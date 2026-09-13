from flask import Flask, render_template, request, redirect, url_for, session
import joblib
import os


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "frontend")
)

# Session use karne ke liye required
app.secret_key = "movie-recommender-secret-key"


MOVIES_PATH = os.path.join(
    BASE_DIR,
    "movies.pkl"
)

SIMILARITY_PATH = os.path.join(
    BASE_DIR,
    "similarity.pkl"
)

MOVIES_RECOMMENDATION_MODEL_PATH = os.path.join(
    BASE_DIR,
    "movies_recommender_system.pkl"
)


# Load files
new_df = joblib.load(MOVIES_PATH)

similarity = joblib.load(SIMILARITY_PATH)


# ---------------------------------------------------
# Recommend function
# ---------------------------------------------------

def recommend(movie):

    movie_index = new_df[
        new_df["title"] == movie
    ].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    data = []

    try:

        for i in movies_list:

            result = new_df.iloc[i[0]].title

            data.append(result)

    except Exception:

        return [
            "Error occurred while fetching recommendations. Please try again."
        ]

    return data


# Load exported recommend function
movies_recommendation_model = joblib.load(
    MOVIES_RECOMMENDATION_MODEL_PATH
)


# ---------------------------------------------------
# Prevent browser from caching old page
# ---------------------------------------------------

@app.after_request
def add_no_cache_headers(response):

    response.headers["Cache-Control"] = (
        "no-store, no-cache, must-revalidate, max-age=0"
    )

    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"

    return response


# ---------------------------------------------------
# Home
# ---------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    # -------------------------
    # User submitted movie
    # -------------------------

    if request.method == "POST":

        movie_name = request.form.get("movie_name")

        if movie_name:

            movie_name = movie_name.strip()

            # Case-insensitive search
            matching_movie = new_df[
                new_df["title"].str.lower()
                == movie_name.lower()
            ]

            if not matching_movie.empty:

                actual_movie_name = matching_movie.iloc[0]["title"]

                predicted_movies = movies_recommendation_model(
                    actual_movie_name
                )

                # Temporarily save recommendations
                session["predicted_movies"] = predicted_movies

            else:

                session["predicted_movies"] = [
                    "Movie not found."
                ]

        else:

            session["predicted_movies"] = [
                "Please enter a movie name."
            ]

        # IMPORTANT:
        # POST ke baad GET request bhejo
        return redirect(url_for("home"))


    # ---------------------------------------------------
    # GET REQUEST
    # Recommendation sirf EK BAAR milegi
    # ---------------------------------------------------

    predicted_movies = session.pop(
        "predicted_movies",
        []
    )


    return render_template(
        "index.html",
        predicted_movies=predicted_movies
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )