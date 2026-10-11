# ML Engineering Projects

This repository contains machine learning engineering projects built using Python, traditional machine learning algorithms, data analysis, recommendation systems, and Flask-based deployment.

The projects demonstrate the complete workflow from data preprocessing and model development to model serialization and deployment as web applications.

## Projects

| Project                                                                         | Area                  | Techniques                                          | Deployment    |
| ------------------------------------------------------------------------------- | --------------------- | --------------------------------------------------- | ------------- |
| [Book Recommender System](./BookRecommenderSystem_MLProject/)                   | Recommendation System | Collaborative Filtering, Cosine Similarity          | Flask         |
| [Customer Churn Prediction](./Customer%20Churn%20Prediction/)                   | Classification        | Traditional ML, Classification                      | Flask         |
| [Customer Segmentation Project using KMeans](./customer-segmentation-kmeans/)  | Clustering            | KMeans Clustering                                   | Flask         |
| [Movie Recommender System](./MovieRecommenderSystem%20MLEngineering%20PROJECT/) | Recommendation System | Content-Based Filtering, NLP, Cosine Similarity     | Flask, Docker |
| [Swiggy Food Intelligence](./Swiggy%20FoodDelivery%20Analysis%20Website/)       | Data Science + ML     | EDA, Hypothesis Testing, Regression, Classification | Flask         |

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* SciPy
* XGBoost
* Matplotlib
* Seaborn
* NLTK
* Joblib
* Pickle
* Flask
* Frontend (HTML,CSS)
* Docker

## Areas Covered

### Data Science

* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Statistical Analysis
* Hypothesis Testing
* Data Visualization
* Regression
* Classification
* Recommendation Systems
* Model Comparison
* Cross-Validation
* Model Evaluation
* Model Serialization

### ML Engineering

* Saving trained ML models
* Loading models for inference
* Flask model serving
* REST API endpoints
* HTML-based ML applications
* Docker containerization

## Repository Structure

```text
MLEngineeringProjects/
│
├── BookRecommenderSystem_MLProject/
│
├── Customer Churn Prediction/
│
├── MovieRecommenderSystem MLEngineering PROJECT/
│
├── Swiggy FoodDelivery Analysis Website/
│
└── README.md
```

## Author

**Om Satyawan Pathak**










# Book Recommender System

A collaborative-filtering-based Book Recommender System built using Python, Pandas, NumPy, and Scikit-learn.

The system uses historical user-book ratings to identify books with similar rating patterns and recommends the top similar books for a selected title.

## Project Overview

The project follows a collaborative filtering approach.

Instead of recommending books only from their metadata, the system uses interactions between users and books.

```text
Books + Users + Ratings
          |
          v
     Data Cleaning
          |
          v
   User/Book Filtering
          |
          v
     Rating Matrix
          |
          v
   Cosine Similarity
          |
          v
 Similar Book Detection
          |
          v
     Top 5 Books
```

## Dataset

The project uses three CSV files:

* `Books.csv`
* `Users.csv`
* `Ratings.csv`

Important information includes:

* Book title
* ISBN
* Book author
* Book cover image URL
* User ID
* Book rating

## Recommendation Approach

### Collaborative Filtering

The recommender identifies books that receive similar ratings from users with sufficient rating activity.

The rating data is filtered to reduce noise and retain books and users with enough interactions.

The final ratings data is converted into a user-book matrix.

```text
                    User 1   User 2   User 3
Book A                 5        0        4
Book B                 4        0        5
Book C                 0        4        4
```

Missing ratings are represented as `0`.

Cosine similarity is then calculated between the book vectors.

```python
similarity_scores = cosine_similarity(pt)
```

For a selected book, the system:

1. Finds the book index.
2. Gets its similarity scores.
3. Sorts books by similarity.
4. Removes the selected book.
5. Returns the top 5 recommendations.

## Filtering

The project filters the dataset to reduce sparse interactions.

Users with more than 200 ratings and books with at least 60 ratings are retained for the recommendation matrix.

This helps create a more useful rating matrix for similarity calculations.

## Model Export

The recommendation system is serialized and stored as:

```text
books_recommender_system.pkl
```

The Flask application loads this exported recommendation system.

## Flask Application

The Flask application is located inside:

```text
book_recommender_flask/
```

Structure:

```text
book_recommender_flask/
│
├── app.py
├── books_recommender_system.pkl
├── requirements.txt
│
├── data/
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

The application:

1. Loads the recommendation system.
2. Receives a book title.
3. Generates recommendations.
4. Displays recommended books.
5. Displays book cover images and additional book information.

## Running the Application

Navigate to:

```bash
cd book_recommender_flask
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Cosine Similarity
* Pickle
* Flask
* HTML
* CSS

## Project Structure

```text
BookRecommenderSystem_MLProject/
│
├── Books.csv
├── Ratings.csv
├── Users.csv
├── final_brs.ipynb
├── final_brs.pdf
├── books_recommender_system.pkl
│
├── book_recommender_flask/
│   ├── app.py
│   ├── requirements.txt
│   ├── books_recommender_system.pkl
│   ├── data/
│   ├── static/
│   └── templates/
│
├── model_deployment/
│   └── upload_model_to_s3.py
│
├── project_demonstration.mp4
└── README.md
```

## Key Learning Outcomes

* Collaborative filtering
* User-book rating matrices
* Sparse data handling
* Cosine similarity
* Recommendation generation
* Model serialization
* Flask integration
* ML model deployment

## Author

**Om Satyawan Pathak**

















# Customer Churn Prediction

A traditional machine learning classification project that predicts whether a telecommunications customer is likely to churn.

The project compares multiple classification algorithms, evaluates their performance using cross-validation, exports the trained model, and integrates the model into a Flask web application.

## Project Overview

```text
Customer Dataset
       |
       v
Data Cleaning
       |
       v
Feature Selection
       |
       v
Train/Test Split
       |
       v
Preprocessing
       |
       +----------------------+
       |                      |
       v                      v
 Numerical               Categorical
 Features                 Features
       |                      |
 StandardScaler        OneHotEncoder
       |                      |
       +----------+-----------+
                  |
                  v
              ML Model
                  |
                  v
          Churn Prediction
                  |
                  v
             Flask App
```

## Dataset

The project uses a Telco Customer Churn dataset.

Important features include:

* Gender
* Partner
* Dependents
* Senior Citizen
* Tenure
* Phone Service
* Internet Service
* Technical Support
* Contract
* Payment Method
* Total Charges
* Streaming TV
* Streaming Movies

The target variable is:

```text
Churn
```

## Data Preprocessing

The project performs:

1. Removal of `customerID`
2. Conversion of `TotalCharges` to numerical format
3. Handling of invalid or missing values
4. Train-test splitting
5. Numerical feature scaling
6. Categorical feature encoding

Numerical features are processed using:

```python
StandardScaler()
```

Categorical features are processed using:

```python
OneHotEncoder()
```

A `ColumnTransformer` is used to combine both preprocessing approaches.

## Machine Learning Algorithms

The project compares:

* Logistic Regression
* K-Nearest Neighbors
* Extra Trees Classifier
* AdaBoost Classifier
* XGBoost Classifier

The models are evaluated using stratified cross-validation.

The recorded notebook results select Logistic Regression as the final model.

## Model Evaluation

Evaluation includes:

* Cross-validation accuracy
* Weighted F1 score
* Test accuracy
* Confusion matrix
* Classification report

Recorded final test performance is approximately:

```text
Test Accuracy: 0.80
Weighted F1 Score: 0.79
```

## Model Export

The trained model is saved as:

```text
CustomerChurnPredictionModel.pkl
```

The exported model contains the preprocessing and classification steps needed for inference.

## Flask Application

The Flask backend is located at:

```text
backend/app.py
```

The frontend is located at:

```text
frontend/index.html
```

The application:

1. Loads the trained model.
2. Receives customer information.
3. Creates a DataFrame from the input.
4. Passes the input through the trained pipeline.
5. Generates the churn prediction.
6. Displays the prediction on the webpage.

## Running the Application

Create a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install flask pandas numpy scikit-learn imbalanced-learn xgboost joblib matplotlib seaborn
```

Run:

```bash
python backend/app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Example Input

```text
Gender: Male
Partner: No
Dependents: Yes
Senior Citizen: 0
Tenure: 22
Phone Service: Yes
Internet Service: Fiber optic
Tech Support: No
Contract: Month-to-month
Payment Method: Credit card (automatic)
Total Charges: 1949.4
Streaming TV: Yes
Streaming Movies: No
```

The application produces a churn classification.

Example:

```text
This customer will NOT churn.
```

or:

```text
This customer WILL churn.
```

## Project Structure

```text
Customer Churn Prediction/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── CustomerChurnPredictionModel.pkl
├── dataset.csv
├── Final_Customer_Churn_Prediction_Classification.ipynb
├── Final_Customer_Churn_Prediction_Classification.pdf
├── customerChurnProjectDemonstration.mp4
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn
* XGBoost
* Matplotlib
* Seaborn
* Joblib
* Flask
* Frontend (HTML, CSS)

## Key Learning Outcomes

* Traditional classification
* Numerical and categorical preprocessing
* Feature scaling
* One-hot encoding
* `ColumnTransformer`
* Stratified cross-validation
* Model comparison
* Classification evaluation
* Confusion matrices
* Model serialization
* Flask model deployment

## Author

**Om Satyawan Pathak**









# Movie Recommender System

A content-based Movie Recommender System that recommends movies based on movie metadata such as overview, genres, keywords, cast, and director.

The project includes a Flask web application and Docker configuration for deploying the recommendation system.

## Project Overview

```text
TMDB Movies + Credits
          |
          v
   Data Preprocessing
          |
          v
   Feature Engineering
          |
          v
    Create Tags
          |
          v
       Stemming
          |
          v
    CountVectorizer
          |
          v
   Movie Vectors
          |
          v
  Cosine Similarity
          |
          v
    Top 5 Movies
          |
          v
      Flask App
          |
          v
   Docker Container
```

## Dataset

The project uses:

```text
tmdb_5000_movies.csv
tmdb_5000_credits.csv
```

The datasets are merged using movie title.

Important columns include:

```text
movie_id
title
overview
genres
keywords
cast
crew
```

## Recommendation Approach

The project uses **content-based filtering**.

Instead of using user ratings, recommendations are generated from the similarity between movie metadata.

The following information is used:

* Movie overview
* Genres
* Keywords
* Cast
* Director

These fields are combined into a single column:

```text
tags
```

## Data Preprocessing

The project performs:

1. Dataset merging
2. Column selection
3. Missing-value handling
4. Duplicate checking
5. Genre extraction
6. Keyword extraction
7. Cast extraction
8. Director extraction
9. Text normalization
10. Creation of the `tags` column

## Stemming

The project uses NLTK's Porter Stemmer to reduce words to common stems.

This helps the recommendation system identify similar words during text matching.

## Text Vectorization

The `tags` column is converted into numerical vectors using:

```python
CountVectorizer(
    max_features=5000,
    stop_words="english"
)
```

The resulting vectors represent the metadata of each movie.

## Cosine Similarity

Cosine similarity is used to calculate the similarity between movie vectors.

```python
similarity = cosine_similarity(vectors)
```

For a selected movie, the recommendation function:

1. Finds the movie index.
2. Retrieves similarity scores.
3. Sorts movies according to similarity.
4. Removes the selected movie.
5. Returns the top 5 similar movies.

## Model Artifacts

The application uses:

```text
movies.pkl
similarity.pkl
movies_recommender_system.pkl
```

These files allow the Flask application to load the processed movie data and similarity information without rebuilding the complete recommendation process.

## Flask Application

Backend:

```text
backend/app.py
```

Frontend:

```text
frontend/index.html
```

The application:

1. Loads the serialized recommendation artifacts.
2. Receives a movie title.
3. Finds the selected movie.
4. Generates recommendations.
5. Displays the recommended movies.

The application also includes session/state handling so previous recommendations are cleared appropriately when the page is refreshed.

## Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask application:

```bash
python backend/app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Docker

Build the image:

```bash
docker build -t movies_recommender_system_project .
```

Run the container:

```bash
docker run -p 5000:5000 movies_recommender_system_project
```

Open:

```text
http://localhost:5000
```

## Project Structure

```text
MovieRecommenderSystem MLEngineering PROJECT/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── Dockerfile
├── requirements.txt
├── movies.pkl
├── similarity.pkl
├── movies_recommender_system.pkl
│
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
│
├── MOVIE RECOMMENDER SYSTEM (Content-Based).ipynb
├── MOVIE RECOMMENDER SYSTEM (Content-Based).pdf
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* CountVectorizer
* Cosine Similarity
* Flask
* Frontend (HTML,CSS)
* Docker

## Key Learning Outcomes

* Content-based recommendation systems
* Text preprocessing
* Feature engineering
* Stemming
* Bag-of-Words
* CountVectorizer
* Cosine similarity
* Recommendation generation
* Model serialization
* Flask deployment
* Docker containerization

## Author

**Om Satyawan Pathak**















# Swiggy Food Intelligence Project

A data science and machine learning project based on Swiggy food-delivery data.

The project combines exploratory data analysis, statistical hypothesis testing, traditional machine learning, model comparison, model serialization, and Flask-based deployment.

## Project Objectives

The project addresses three major machine learning problems:

1. Predict restaurant delivery time.
2. Classify restaurants as Fast or Slow delivery.
3. Classify restaurants into Premium or Budget price segments.

The project also uses statistical hypothesis testing to investigate relationships between delivery time, ratings, cuisines, and cities.

## Workflow

```text
Swiggy Dataset
      |
      v
Data Cleaning
      |
      +--------------------+
      |                    |
      v                    v
     EDA            Hypothesis Testing
      |                    |
      +---------+----------+
                |
                v
       Feature Engineering
                |
                v
        Traditional ML
          /         \
         /           \
 Regression       Classification
     |                 |
     v                 v
Delivery Time     Price Segment
Prediction        Prediction
     |
     v
Model Export
     |
     v
Flask Application
```

## Dataset

The main dataset is:

```text
dataset/swiggy.csv
```

Important features include:

* Area
* City
* Restaurant
* Price
* Average ratings
* Total ratings
* Address
* Food type
* Delivery time

## Exploratory Data Analysis

The project performs analysis of:

* Delivery-time distribution
* Restaurant prices
* Average ratings
* Total ratings
* Food types
* City-level patterns
* Relationships between price and ratings
* Relationships between ratings and delivery time

Visualizations are created using:

* Matplotlib
* Seaborn

## Hypothesis Testing

The project applies multiple statistical tests.

### One-Sample t-Test

Tests whether the average delivery time differs from a benchmark of 45 minutes.

### Welch's Two-Sample t-Test

Compares average delivery times between Indian and Chinese restaurants.

### One-Sample t-Test for Ratings

Tests whether the average restaurant rating differs from 4.0.

### Welch's Two-Sample t-Test for Ratings

Compares ratings between Indian and Chinese restaurants.

### One-Way ANOVA

Tests whether average delivery time differs among:

* Indian
* Chinese
* Fast Food

restaurants.

### Chi-Square Test

Tests the relationship between:

```text
City
```

and:

```text
Food Type
```

The notebook uses:

```text
alpha = 0.05
```

where applicable.

## Machine Learning

### 1. Delivery Time Prediction

The project predicts delivery time using restaurant, pricing, rating, and location information.

Regression algorithms compared include:

* Linear Regression
* K-Nearest Neighbors Regressor
* Decision Tree Regressor
* Extra Trees Regressor
* AdaBoost Regressor
* XGBoost Regressor

Models are evaluated using:

* R²
* Mean Absolute Error
* Root Mean Squared Error

The recorded notebook results identify XGBoost as the selected regression model, with an R² of approximately 0.67.

The trained model is stored as:

```text
Swiggy_FoodDeliveryTimePrediction_Model.pkl
```

### 2. Fast vs Slow Delivery

A delivery-speed target is created using the median delivery time.

```text
Fast -> delivery time <= median
Slow -> delivery time > median
```

The project investigates relationships between delivery speed and:

* Price
* Average rating
* Total ratings

A Decision Tree Classifier is used for this task.

### 3. Premium vs Budget

A price segment is created using restaurant price:

```text
Premium -> Price > 500
Budget  -> Price <= 500
```

The classification models are compared and the trained model is exported as:

```text
Price_Classification.pkl
```

The recorded notebook results report approximately 89% classification accuracy for the selected approach.

## Flask Deployment

The Flask backend is located at:

```text
backend/app.py
```

The frontend is located at:

```text
frontend/index.html
```

The application loads:

```text
Swiggy_FoodDeliveryTimePrediction_Model.pkl
Price_Classification.pkl
```

## API Endpoints

### Home

```http
GET /
```

Loads the main web interface.

### Delivery Time Prediction

```http
POST /predict
```

Expected input fields include:

```text
Area
City
Restaurant
Price
Avg ratings
Total ratings
Address
```

The endpoint returns a predicted delivery time.

Example:

```json
{
    "predicted_delivery_time": 51.2,
    "prediction": 51.2
}
```

### Price Segment Prediction

```http
POST /predict-price-segment
```

Expected fields include:

```text
Area
City
Restaurant
Avg ratings
Total ratings
Food type
Address
```

Example response:

```json
{
    "price_segment": "Premium",
    "prediction": "Premium"
}
```

## Running the Application

Create a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install flask pandas numpy scikit-learn xgboost joblib
```

Run:

```bash
python backend/app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
Swiggy FoodDelivery Analysis Website/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── dataset/
│   └── swiggy.csv
│
├── Price_Classification.pkl
├── Swiggy_FoodDeliveryTimePrediction_Model.pkl
│
├── source_code_swiggy.ipynb
├── source_code_swiggy.pdf
├── swiggy_fdAnalysis_project_demonstration.mp4
└── README.md
```

## Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

### Machine Learning

* Scikit-learn
* XGBoost

### Deployment

* Joblib
* Flask
* Frontend (HTML,CSS)

## Key Learning Outcomes

* Exploratory Data Analysis
* Statistical hypothesis testing
* t-tests
* ANOVA
* Chi-Square testing
* Regression
* Classification
* Cross-validation
* Traditional machine learning
* Model comparison
* Model serialization
* Flask APIs
* Machine learning deployment

## Author

**Om Satyawan Pathak**

Email: [omsatyawanpathakgit@gmail.com](mailto:omsatyawanpathakgit@gmail.com)

