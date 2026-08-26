#  Book Recommender System

An end-to-end book recommendation project that combines a **popularity-based recommender** with an **item-based collaborative filtering model**.  
Originally developed in Python and later converted into a **Flask web application**, this system allows users to browse popular books and receive five similar-book recommendations through a website.

---

##  Project Overview

Online book catalogues can contain hundreds of thousands of titles, making it difficult for readers to decide what to read next.  
This project reduces that search effort by learning patterns from historical user ratings.

The system provides two recommendation experiences:
- **Popular Books** → Displays highly rated books with at least 250 ratings.
- **Similar Book Recommendations** → Accepts a selected book and returns the five most similar books based on user-rating behaviour.

Similarity is determined by **collaborative filtering** (user ratings), not by book descriptions, genres, or keywords.

---

##  Key Features

- Loads and processes book, user, and rating data.
- Cleans missing values and standardizes user-location text.
- Identifies the **50 most popular books** using rating count and average rating.
- Retains **active users** (≥200 ratings) and **frequently rated books** (≥60 ratings).
- Creates a **book-user ratings matrix** with Pandas pivot tables.
- Calculates **cosine similarity** between books.
- Returns five recommendations with **ISBN, title, author, and cover image**.
- Serializes recommendation logic/artifacts for reuse.
- Exposes the recommender through a **Flask-based website**.

---

##  Recommendation Approach

### 1. Popularity-Based Recommendation
- Groups ratings by book title.
- Calculates:
  - `num_ratings`: total ratings per title
  - `avg_rating`: mean rating per title
- Retains books with ≥250 ratings.
- Displays **Top 50 books** sorted by average rating.

### 2. Collaborative Filtering
- Active users: ≥200 ratings.
- Books retained: ≥60 ratings from active users.
- Pivot table: 500 books × 808 users.
- Cosine similarity applied to book vectors.
- Returns **five most similar books** for a given title.

---

