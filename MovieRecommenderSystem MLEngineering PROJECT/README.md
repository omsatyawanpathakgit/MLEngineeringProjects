# Movie Recommender System — Content-Based Filtering + Docker

A content-based Movie Recommender System that recommends similar movies based on movie metadata such as overview, genres, keywords, cast, and director.

This project was originally developed as a Data Science project and was later revisited and containerized using Docker to make the application easier to package, run, and deploy consistently across different environments.

While revisiting the project, I also addressed an important application-level issue that I had overlooked in some of my earlier recommender projects: session/state handling. Previous recommendation results should not remain visible after a page refresh or a new interaction unless they are intentionally preserved. The application now resets stale recommendation state appropriately so that the UI reflects the current user interaction.

## Project Overview:

The recommendation engine follows a content-based filtering approach.

Instead of relying on ratings from other users, the system compares movies using their own characteristics. Movie information is converted into text-based feature representations, transformed into numerical vectors, and compared using cosine similarity.

When a user selects a movie, the system returns the movies with the highest similarity scores.

Core workflow

Movie Metadata
      ↓
Data Cleaning & Feature Selection
      ↓
Feature Engineering
      ↓
Combined "tags" Feature
      ↓
Text Preprocessing + Stemming
      ↓
CountVectorizer
      ↓
Movie Vectors
      ↓
Cosine Similarity Matrix
      ↓
Top Similar Movies
      ↓
Recommendation Results

## Project Objectives:

The main objectives of this project are to:

Build a movie recommendation engine using content-based filtering

Combine meaningful movie metadata into a single feature representation

Convert text features into numerical vectors

Calculate similarity between movies using cosine similarity

Recommend the most similar movies for a selected title

Export the trained recommendation artifacts for application use

Improve application behavior through proper session/state handling

Package the complete application using Docker

Make the project easier to reproduce and deploy across systems

## Recommendation Approach:

Content-Based Filtering

A content-based recommender suggests items based on the characteristics of the items themselves.

For this project, each movie is represented using information such as:

Movie overview

Genres

Keywords

Top cast members

Director

These features are combined into a single textual representation called tags.

The system then compares the selected movie with all other movies and returns the most similar ones.

## Dataset:

The project uses the TMDB 5000 movie dataset:

tmdb_5000_movies.csv
tmdb_5000_credits.csv

The two datasets are merged using the movie title.

After merging, the project keeps the following useful fields:

movie_id
title
overview
genres
keywords
cast
crew

## Data Preprocessing:

The preprocessing pipeline includes the following steps.

1. Merge the datasets

The movie and credits datasets are merged using:

movies = movies.merge(credits, on="title")

2. Keep relevant columns

movies = movies[
    ["movie_id", "title", "overview", "genres", "keywords", "cast", "crew"]
]

3. Handle missing values

Rows containing missing values are removed.

movies.dropna(inplace=True)

4. Check duplicate records

Duplicate movie records are checked before continuing.

5. Extract genres and keywords

The original dataset stores these fields in structured text form.

The project extracts only the corresponding names.

Example:

Action
Adventure
Fantasy
Science Fiction

6. Keep the first three cast members

Only the first three actors are retained from the cast information.

7. Extract the director

From the crew information, only the person whose job is Director is retained.

8. Normalize multi-word entities

Whitespace is removed from multi-word values so that names such as:

Sam Worthington
Science Fiction
James Cameron

become:

SamWorthington
ScienceFiction
JamesCameron

This prevents separate words from being interpreted as unrelated features.

## Feature Engineering:

The project combines the following columns:

overview
genres
keywords
cast
crew

into a new column named: tags

The final working DataFrame contains:

movie_id
title
tags

The tags values are then converted into lowercase strings.

## Stemming:

The project uses the Porter Stemmer from NLTK.

Stemming reduces related words to a common root form.

### For example:

love
loved
loving

can be reduced toward a common stem.

Implementation:

from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def stem(text):
    words = []

    for word in text.split():
        words.append(ps.stem(word))

    return " ".join(words)

The stemming function is then applied to the tags column.

## Text Vectorization:

The project uses Bag of Words through Scikit-learn's CountVectorizer.

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

The movie tags are transformed into numerical vectors:

vectors = cv.fit_transform(new_df["tags"]).toarray()

The project uses a maximum vocabulary size of:

5000 features

and removes English stop words.

The resulting vector representation has approximately:

4806 movies × 5000 features

## Cosine Similarity:

After vectorization, the similarity between every movie and every other movie is calculated using cosine similarity.

from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

The resulting similarity matrix has approximately:

4806 × 4806

Each value represents how similar one movie is to another based on the engineered content features.

## Recommendation Logic:

The recommendation function performs the following steps:

Receive a movie title

Find the movie's DataFrame index

Retrieve that movie's similarity scores

Pair every movie index with its score

Sort the movies by similarity in descending order

Ignore the selected movie itself

Return the top 5 most similar movies

Simplified logic:

def recommend(movie):
    movie_index = new_df[new_df["title"] == movie].index[0]

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
        print("No recommendations were found for this movie.")

    return data

## Example Recommendations:

Input

Avatar

Example output

Aliens vs Predator: Requiem
Aliens
Falcon Rising
Independence Day
Titan A.E.

Another test in the original project uses:

Batman Begins

and returns similar Batman-related movies among the recommendations.


## Exported Recommendation Artifacts:

The project exports the processed movie data, similarity matrix, and recommendation function using pickle.

Movie DataFrame

pickle.dump(
    new_df,
    open("movies.pkl", "wb")
)

Similarity Matrix

pickle.dump(
    similarity,
    open("similarity.pkl", "wb")
)

Recommendation Function

with open("movies_recommender_system.pkl", "wb") as f:
    pickle.dump(recommend, f)

These files can then be loaded by the application without rebuilding the recommendation pipeline every time the app starts.

## Session / State Handling Improvement:

One of the important improvements made while revisiting this project was proper recommendation state management.

In some of my earlier recommender applications, recommendation results could remain visible even after the page was refreshed.

For example:

User searches: Book 1
        ↓
Recommendations are displayed
        ↓
Page is refreshed
        ↓
Old recommendations remain visible

This is undesirable because the UI can display stale results that no longer represent the current user interaction.

Improved behavior

The application now ensures that old recommendation data is reset when appropriate.

Conceptually:

Initial state
recommendations = null

        ↓

User selects a movie

        ↓

Generate recommendations

        ↓

Display current results

        ↓

Refresh / reset / new clean state

        ↓

recommendations = null

This improvement helped me understand that a recommendation system is not only about the machine learning logic. A reliable user-facing application also requires correct application state management.

## Dockerization:

The complete application has been containerized using Docker.

Docker packages the application together with its dependencies so that it can run consistently across different machines and environments.

Why Docker?

Without containerization, differences in:

Python versions

Installed libraries

Operating systems

Environment configuration

can cause an application to behave differently on another machine.

Docker provides a reproducible environment for the project.

## Docker Workflow:

Source Code
   +
Python Dependencies
   +
Recommendation Artifacts
   +
Application Files
       ↓
   Dockerfile
       ↓
   Docker Image
       ↓
   Docker Container
       ↓
Running Movie Recommender Application

## Running the Project with Docker:

docker run -p 5000:5000 movies_recommender_system_project


## Technologies Used:

Category

Technology

Programming Language

Python

Data Manipulation

Pandas, NumPy
Feature Extraction

CountVectorizer

Similarity Algorithm

Cosine Similarity

Machine Learning Library

Scikit-learn

Model Serialization

Pickle

Dataset

TMDB 5000 Movies & Credits

Containerization

Docker

## Python Dependencies:

Install dependencies locally using:

pip install -r requirements.txt

## How the Complete System Works

              ┌─────────────────────┐
              │    TMDB Datasets    │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Data Preprocessing│
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Feature Engineering│
              │      "tags"         │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │      Stemming       │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   CountVectorizer   │
              │  Bag-of-Words Model │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │   Movie Vectors     │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Cosine Similarity   │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Recommendation Logic│
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │ Application + State │
              │     Management      │
              └──────────┬──────────┘
                         │
                         ▼
              ┌─────────────────────┐
              │  Docker Container   │
              └─────────────────────┘

## Key Learnings:

This project helped strengthen my understanding of both the Data Science and application deployment sides of a recommendation system.

Key learnings include:

Understanding different recommendation system approaches

Building a content-based recommender from movie metadata

Cleaning and transforming semi-structured movie information

Creating meaningful combined text features

Applying NLP preprocessing and stemming

Using Bag of Words for text vectorization

Understanding cosine similarity in high-dimensional feature spaces

Ranking movies using similarity scores

Exporting processed data and recommendation artifacts

Integrating a Data Science model into an application

Recognizing the importance of session/state management

Avoiding stale recommendation results after refresh/reset events

Packaging a complete project using Docker

Improving reproducibility and deployment consistency

## Potential Future Improvements:

Possible future improvements include:

Add movie posters and richer metadata

Add fuzzy search or autocomplete for movie names

Improve handling of movies not found in the dataset

Add pagination or configurable recommendation counts

Compare Bag of Words with TF-IDF

Experiment with richer semantic embeddings

Add collaborative filtering

Build a hybrid recommendation system

Add automated tests for recommendation logic

Add Docker Compose if the project expands to multiple services

Add CI/CD for automated image builds and deployment

Add logging and health checks

Add persistent user profiles if personalized history is required

## Limitations:

This project uses content-based similarity, so recommendations depend entirely on the metadata available for each movie.

Some limitations are:

No user-specific rating history

No collaborative behavior between users

Recommendation quality depends on the quality of movie metadata

Bag-of-Words vectors do not capture deep semantic meaning

Similar titles or duplicated dataset records may influence results

The system recommends based on similarity, not individual long-term preferences






## Author:

### Name: Om Satyawan Pathak

### Email: omsatyawanpathakgit@gmail.com

### LinkedIn: https://www.linkedin.com/in/om-satyawan-pathak-029b02368/

## Final Note:

This project began as a Data Science implementation of a content-based Movie Recommender System and later became an opportunity to improve the complete application lifecycle.

Revisiting the project helped me move beyond only building the recommendation model and focus on two practical software considerations:

State/session handling so that recommendation results remain consistent with the user's current interaction.

Docker containerization so that the application can be packaged and executed consistently across environments.

It was a useful reminder that building a successful Data Science application involves not only model logic, but also reliable application behavior, reproducibility, and deployment.