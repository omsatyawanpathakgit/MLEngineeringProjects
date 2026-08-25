import csv
import os
import pickle
from collections import Counter, defaultdict

import pandas as pd
from flask import Flask, render_template, request


app = Flask(__name__)


# =========================================================
# LOAD RECOMMENDATION MODEL
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOKS_PATH = os.path.join(BASE_DIR, "data", "Books.csv")
RATINGS_PATH = os.path.join(BASE_DIR, "data", "Ratings.csv")


def _load_recommendation_data():
    books = {}
    with open(BOOKS_PATH, encoding="latin-1", newline="") as file:
        for row in csv.reader(file):
            if not row or row[0] == "ISBN":
                continue

            if len(row) < 7:
                continue
            isbn = row[0].strip()
            author = row[-6].strip()
            title = ",".join(row[1:-6]).strip()
            books[isbn] = (title, author, row[-3])

    ratings = pd.read_csv(RATINGS_PATH, encoding="latin-1")
    ratings = ratings[ratings["Book-Rating"] > 0]
    users_by_isbn = defaultdict(set)
    isbns_by_user = defaultdict(set)
    for user_id, isbn in ratings[["User-ID", "ISBN"]].itertuples(index=False):
        isbn = str(isbn).strip()
        if isbn in books:
            users_by_isbn[isbn].add(user_id)
            isbns_by_user[user_id].add(isbn)

    return books, users_by_isbn, isbns_by_user


BOOKS, USERS_BY_ISBN, ISBNS_BY_USER = _load_recommendation_data()


def recommend_books(book_name, limit=5):
    """Return books that share the most positively rating users."""
    matching_isbns = [
        isbn for isbn, (title, _, _) in BOOKS.items()
        if title.casefold() == book_name.casefold()
    ]
    if not matching_isbns:
        matching_isbns = [
            isbn for isbn, (title, _, _) in BOOKS.items()
            if book_name.casefold() in title.casefold()
        ]
    if not matching_isbns:
        return []

    candidate_counts = Counter()
    for isbn in matching_isbns:
        for user_id in USERS_BY_ISBN[isbn]:
            candidate_counts.update(ISBNS_BY_USER[user_id])
    for isbn in matching_isbns:
        candidate_counts.pop(isbn, None)

    recommendations = []
    for isbn, _ in candidate_counts.most_common(limit):
        title, author, image = BOOKS[isbn]
        recommendations.append((isbn, title, author, image))
    return recommendations


class _RecommendationModelUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__" and name == "recommend_books":
            return recommend_books
        return super().find_class(module, name)


with open(os.path.join(BASE_DIR, "books_recommender_system.pkl"), "rb") as f:
    model = _RecommendationModelUnpickler(f).load()


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    selected_book = ""
    error = None


    if request.method == "POST":

        selected_book = request.form.get("book_name", "").strip()

        if not selected_book:
            error = "Please enter a book name."
            return render_template(
                "index.html",
                recommendations=recommendations,
                selected_book=selected_book,
                error=error
            )


        try:

            # -----------------------------------------
            # FETCH RECOMMENDATIONS DIRECTLY
            # FROM YOUR EXPORTED MODEL
            # -----------------------------------------

            result = model(selected_book)


            # Your model returns:
            #
            # [
            #   [
            #       ISBN,
            #       Book-Title,
            #       Book-Author,
            #       Image-URL
            #   ],
            #   ...
            # ]


            for book in result:

                isbn = str(book[0])

                recommendations.append({

                    "isbn": isbn,

                    "title": book[1],

                    "author": book[2],

                    "image": book[3],

                    "amazon_url":
                        f"https://www.amazon.com/dp/{isbn}"

                })


            if len(recommendations) == 0:

                error = "No recommendations found."


        except Exception:

            error = (
                "Book not found in the recommendation system."
            )


    return render_template(

        "index.html",

        recommendations=recommendations,

        selected_book=selected_book,

        error=error

    )


# =========================================================
# START FLASK
# =========================================================

if __name__ == "__main__":

    app.run(debug=True)