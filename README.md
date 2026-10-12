# ML Engineering Projects

This repository contains machine learning engineering projects built using Python, traditional machine learning algorithms, data analysis, recommendation systems, and Flask-based deployment.

The projects demonstrate the complete workflow, from data preprocessing and model development to model serialization and deployment as web applications.

## Projects

| Project | Area | Techniques | Deployment |
|---|---|---|---|
| [Book Recommender System](./BookRecommenderSystem_MLProject/) | Recommendation System | Collaborative Filtering, Cosine Similarity | Flask |
| [Customer Churn Prediction](./Customer%20Churn%20Prediction/) | Classification | Traditional ML, Classification | Flask |
| [Customer Segmentation Using K-Means](./customer-segmentation-kmeans/) | Clustering | K-Means, StandardScaler, Elbow Method, Silhouette Score | Flask, Vercel |
| [Movie Recommender System](./MovieRecommenderSystem%20MLEngineering%20PROJECT/) | Recommendation System | Content-Based Filtering, NLP, Cosine Similarity | Flask, Docker |
| [Swiggy Food Intelligence](./Swiggy%20FoodDelivery%20Analysis%20Website/) | Data Science and ML | EDA, Hypothesis Testing, Regression, Classification | Flask |

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- XGBoost
- Matplotlib
- Seaborn
- NLTK
- Joblib
- Pickle
- Flask
- HTML and CSS
- Docker
- Vercel

## Areas Covered

### Data Science

- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Statistical Analysis
- Hypothesis Testing
- Data Visualization
- Regression
- Classification
- Clustering
- Recommendation Systems
- Model Comparison
- Cross-Validation
- Model Evaluation
- Model Serialization

### ML Engineering

- Saving trained ML models
- Loading models for inference
- Flask model serving
- REST API endpoints
- HTML-based ML applications
- Scikit-learn pipelines
- Docker containerization
- Machine learning deployment

---

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

- `Books.csv`
- `Users.csv`
- `Ratings.csv`

Important information includes:

- Book title
- ISBN
- Book author
- Book cover image URL
- User ID
- Book rating

## Recommendation Approach

### Collaborative Filtering

The recommender identifies books that receive similar ratings from users with sufficient rating activity.

The rating data is filtered to reduce noise and retain books and users with enough interactions.

The final ratings data is converted into a user-book matrix.

```text
          User 1   User 2   User 3
Book A      5        0        4
Book B      4        0        5
Book C      0        4        4
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
5. Returns the top five recommendations.

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
├── app.py
├── books_recommender_system.pkl
├── requirements.txt
├── data/
│   ├── Books.csv
│   ├── Ratings.csv
│   └── Users.csv
├── static/
│   └── style.css
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

Navigate to the application directory:

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

Run the application:

```bash
python app.py
```

Open the application at:

http://127.0.0.1:5000

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Cosine Similarity
- Pickle
- Flask
- HTML
- CSS

## Project Structure

```text
BookRecommenderSystem_MLProject/
├── Books.csv
├── Ratings.csv
├── Users.csv
├── final_brs.ipynb
├── final_brs.pdf
├── books_recommender_system.pkl
├── book_recommender_flask/
│   ├── app.py
│   ├── requirements.txt
│   ├── books_recommender_system.pkl
│   ├── data/
│   ├── static/
│   └── templates/
├── model_deployment/
│   └── upload_model_to_s3.py
├── project_demonstration.mp4
└── README.md
```

## Key Learning Outcomes

- Collaborative filtering
- User-book rating matrices
- Sparse data handling
- Cosine similarity
- Recommendation generation
- Model serialization
- Flask integration
- ML model deployment

---

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
 Numerical              Categorical
  Features               Features
       |                      |
       v                      v
 StandardScaler         OneHotEncoder
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

- Gender
- Partner
- Dependents
- Senior Citizen
- Tenure
- Phone Service
- Internet Service
- Technical Support
- Contract
- Payment Method
- Total Charges
- Streaming TV
- Streaming Movies

The target variable is:

```text
Churn
```

## Data Preprocessing

The project performs:

1. Removal of `customerID`.
2. Conversion of `TotalCharges` to numerical format.
3. Handling of invalid or missing values.
4. Train-test splitting.
5. Numerical feature scaling.
6. Categorical feature encoding.

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

- Logistic Regression
- K-Nearest Neighbors
- Extra Trees Classifier
- AdaBoost Classifier
- XGBoost Classifier

The models are evaluated using stratified cross-validation.

The recorded notebook results select Logistic Regression as the final model.

## Model Evaluation

Evaluation includes:

- Cross-validation accuracy
- Weighted F1 score
- Test accuracy
- Confusion matrix
- Classification report

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

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install flask pandas numpy scikit-learn imbalanced-learn xgboost joblib matplotlib seaborn
```

Run the application from the project root:

```bash
python backend/app.py
```

Open the application at:

http://127.0.0.1:5000

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

Possible outputs:

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
├── backend/
│   └── app.py
├── frontend/
│   └── index.html
├── CustomerChurnPredictionModel.pkl
├── dataset.csv
├── Final_Customer_Churn_Prediction_Classification.ipynb
├── Final_Customer_Churn_Prediction_Classification.pdf
├── customerChurnProjectDemonstration.mp4
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- XGBoost
- Matplotlib
- Seaborn
- Joblib
- Flask
- HTML
- CSS

## Key Learning Outcomes

- Traditional classification
- Numerical and categorical preprocessing
- Feature scaling
- One-hot encoding
- `ColumnTransformer`
- Stratified cross-validation
- Model comparison
- Classification evaluation
- Confusion matrices
- Model serialization
- Flask model deployment

---

# Customer Segmentation Project Using K-Means

A machine learning project that performs customer segmentation using the K-Means Clustering algorithm.

The objective is to divide mall customers into meaningful groups based on their annual income and spending behaviour. These segments can help businesses understand different customer groups and develop targeted marketing strategies.

The project covers exploratory data analysis, feature selection, feature scaling, optimal cluster selection, clustering evaluation, pipeline construction, model serialization, and deployment through a Flask web application on Vercel.

## Project Objectives

The main objectives are:

- Explore customer demographics, income, and spending behaviour.
- Identify meaningful customer segments using unsupervised learning.
- Select suitable clustering features for segmentation.
- Determine an appropriate number of clusters.
- Evaluate clustering quality using the Elbow Method and Silhouette Score.
- Build a reusable scikit-learn pipeline.
- Save the trained pipeline for future predictions.
- Integrate the clustering model into a Flask web application.
- Deploy the application using Vercel.

## Project Workflow

```text
Mall Customers Dataset
          |
          v
     Data Loading
          |
          v
     Data Cleaning
          |
          v
Exploratory Data Analysis
          |
          v
    Feature Selection
          |
          v
   Feature Scaling
    StandardScaler
          |
          v
 Determine Optimal K
  |               |
  v               v
Elbow Method   Silhouette Score
  |               |
  +-------+-------+
          |
          v
   K-Means Clustering
          |
          v
  Customer Segments
          |
          v
 Clustering Evaluation
          |
          v
 Pipeline Construction
          |
          v
  Model Serialization
          |
          v
    Flask Application
          |
          v
   Vercel Deployment
```

## Dataset

The project uses the Mall Customers dataset.

Dataset file:

```text
Mall_Customers.csv
```

The dataset contains customer demographic information and spending-related features.

Important columns include:

| Column | Description |
|---|---|
| `CustomerID` | Unique identifier assigned to each customer |
| `Gender` | Customer gender |
| `Age` | Customer age |
| `Annual Income (k$)` | Annual income measured in thousands of dollars |
| `Spending Score (1-100)` | Spending score assigned to the customer |

The main segmentation analysis uses:

- `Annual Income (k$)`
- `Spending Score (1-100)`

These two features are used to identify groups with different income and spending patterns.

`CustomerID` is an identifier rather than a meaningful clustering feature. Gender and age can be explored during EDA but are not included in the two-feature clustering model described here.

## Exploratory Data Analysis

Exploratory Data Analysis is performed to understand the dataset before applying K-Means Clustering.

### 1. Dataset Inspection

The dataset is inspected to understand its structure and contents.

Typical operations include:

- Viewing the first few rows.
- Checking the number of rows and columns.
- Examining data types.
- Checking for missing values.
- Checking for duplicate records.
- Generating descriptive statistics.

These checks help identify potential data-quality issues before modelling.

### 2. Customer Demographics

The project explores customer demographic characteristics, including:

- Gender distribution
- Age distribution
- Age-related patterns in the dataset

These analyses provide context about the customers represented in the dataset.

### 3. Income Analysis

Annual income is examined to understand how income varies across customers.

The analysis can include:

- Distribution of annual income.
- Minimum and maximum income.
- Average and median income.
- Spread of income values.

This helps explain the income patterns represented in the dataset.

### 4. Spending Score Analysis

The spending score is examined to understand customer spending behaviour.

The analysis considers:

- Distribution of spending scores.
- Low and high spending patterns.
- Differences in spending behaviour across the dataset.

### 5. Correlation Analysis

Correlation between numerical features is examined using a correlation matrix and heatmap.

This helps explore relationships between age, annual income, and spending score.

Correlation analysis is exploratory and does not, by itself, determine the optimal number of clusters.

### 6. Income vs. Spending Score

A scatter plot is created using annual income and spending score.

This is an important visualization because these are the two features used for clustering.

The plot helps identify visible patterns, such as:

- Customers with low income and low spending scores.
- Customers with low income and high spending scores.
- Customers with high income and low spending scores.
- Customers with high income and high spending scores.
- Customers with moderate income and spending scores.

These patterns provide an initial understanding of the potential customer segments.

## Feature Selection

The project selects two features for the K-Means model:

```python
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
```

### Why These Features?

Annual income provides an indication of customers' financial capacity, while spending score represents their spending behaviour.

Using both features makes it possible to segment customers according to two different business dimensions.

The `CustomerID` column is excluded because it is only an identifier. Gender and age are also excluded from the clustering input so that the model focuses specifically on income and spending behaviour.

## Feature Scaling

K-Means Clustering uses distances between data points to assign customers to clusters.

Because annual income and spending score can have different numerical ranges and distributions, feature scaling is applied before clustering.

The project uses `StandardScaler`:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

StandardScaler transforms each feature to have approximately zero mean and unit variance.

### Why Is Scaling Important?

Without scaling, a feature with a larger numerical spread can have a greater influence on the distance calculations.

Scaling helps ensure that both selected features contribute more comparably to the clustering process.

The scaler must be fitted on the training or reference data and reused when transforming new customer inputs. It should not be independently fitted on each new prediction.

## Determining the Optimal Number of Clusters

The project uses two methods to help determine the appropriate number of clusters:

1. Elbow Method using Within-Cluster Sum of Squares (WCSS).
2. Silhouette Score.

Both methods provide information about clustering quality, but they measure different properties.

### 1. Elbow Method

The Elbow Method evaluates K-Means models with different numbers of clusters.

For each value of \(K\), the model's inertia, also known as WCSS, is recorded.

Inertia measures the sum of squared distances between data points and their assigned cluster centres.

Example:

```python
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

wcss = []

for k in range(1, 11):
    kmeans = KMeans(
        n_clusters=k,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()
```

As the number of clusters increases, inertia generally decreases because each cluster can represent a smaller group of observations.

The preferred value is often near the point where the reduction in inertia begins to slow down significantly. This point is known as the elbow.

### 2. Silhouette Score

The Silhouette Score evaluates how well each observation fits within its assigned cluster compared with other clusters.

The score ranges from -1 to 1.

| Score | Interpretation |
|---|---|
| Close to 1 | Observations are generally well matched to their assigned clusters and separated from other clusters |
| Close to 0 | Clusters overlap or observations lie near cluster boundaries |
| Below 0 | Some observations may be closer to another cluster than to their assigned cluster |

A higher average silhouette score generally indicates better-separated clusters.

Example:

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

for k in range(2, 11):
    kmeans = KMeans(
        n_clusters=k,
        init='k-means++',
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, labels)

    print(f'K = {k}, Silhouette Score = {score:.4f}')
```

The Silhouette Score cannot be calculated meaningfully for a clustering result with only one cluster, which is why the evaluation starts at \(K=2\).

### Selecting K

The project selects **K = 5** based on the recorded Elbow Method and Silhouette Score analysis.

The Elbow Method helps identify diminishing returns from adding clusters, while the Silhouette Score evaluates cluster cohesion and separation.

The two methods should be considered together with the business interpretability of the resulting segments rather than treating either metric as an absolute rule.

## K-Means Clustering

K-Means is an unsupervised machine learning algorithm that partitions observations into a specified number of clusters.

The algorithm works iteratively:

1. Initializes cluster centres.
2. Assigns each customer to the nearest cluster centre.
3. Recalculates the cluster centres based on the assigned customers.
4. Repeats the assignment and update steps until convergence or the iteration limit is reached.

The project uses five clusters.

Example:

```python
from sklearn.cluster import KMeans

kmeans = KMeans(
    n_clusters=5,
    init='k-means++',
    random_state=42,
    n_init=10
)

labels = kmeans.fit_predict(X_scaled)
```

The `n_clusters=5` parameter specifies the number of clusters.

The `init='k-means++'` parameter uses an initialization strategy designed to spread the initial cluster centres.

The `random_state=42` parameter helps make results reproducible, while `n_init=10` runs multiple initializations and selects the solution with the lowest inertia.

## Customer Segments

The five clusters are interpreted using their annual income and spending score characteristics.

| Cluster | Segment Interpretation | Potential Business Insight |
|---|---|---|
| 0 | Moderate-Income, Moderate-Spending Customers | May respond to loyalty programmes and offers that encourage repeat purchases |
| 1 | High-Income, High-Spending Customers | May be suitable for premium products, exclusive offers, and loyalty benefits |
| 2 | Low-Income, High-Spending Customers | May respond to affordable premium options, promotions, and value-oriented products |
| 3 | High-Income, Low-Spending Customers | May be suitable for personalized promotions and campaigns designed to encourage engagement |
| 4 | Low-Income, Low-Spending Customers | May respond to discounts, budget-friendly products, and essential offers |

**Note:** These are business-oriented interpretations of the recorded cluster labels. Cluster numbers are arbitrary identifiers assigned by K-Means, not fixed customer categories. The actual characteristics of each cluster should be confirmed by examining the fitted cluster centres in the original feature units.

## Visualizing the Clusters

A scatter plot can be used to visualize the resulting customer segments.

The horizontal axis represents annual income, and the vertical axis represents spending score.

Each customer is displayed according to the cluster assigned by the K-Means model.

Cluster centres can also be plotted to show the approximate central position of each segment.

This visualization helps assess whether the identified groups are reasonably separated and whether their characteristics make sense from a business perspective.

## Building the Scikit-Learn Pipeline

The project exports the complete customer segmentation workflow as a scikit-learn pipeline.

The pipeline combines:

1. StandardScaler for feature scaling.
2. K-Means for clustering.

Example:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('kmeans', KMeans(
        n_clusters=5,
        init='k-means++',
        random_state=42,
        n_init=10
    ))
])
```

The pipeline can be fitted on the selected features:

```python
pipeline.fit(X)
```

The fitted pipeline stores the scaler parameters and K-Means model.

When new customer data is passed through the pipeline, the scaler transforms the input before K-Means assigns it to a cluster.

For example:

```python
new_customer = [[75, 60]]

cluster = pipeline.predict(new_customer)

print(cluster)
```

The example represents an annual income of 75 thousand dollars and a spending score of 60. The resulting cluster depends on the fitted model and dataset.

**Important:** The example assumes that the pipeline has already been fitted on the original dataset and that incoming values use the same feature order and units.

## Model Serialization

The complete fitted pipeline is exported so that the Flask application can use the trained model without retraining it whenever a request arrives.

The exported model is saved as:

```text
complete_customer_segmentation_pipeline.pkl
```

The pipeline can be serialized using Joblib:

```python
import joblib

joblib.dump(
    pipeline,
    'complete_customer_segmentation_pipeline.pkl'
)
```

It can later be loaded for inference:

```python
pipeline = joblib.load(
    'complete_customer_segmentation_pipeline.pkl'
)
```

Saving the entire pipeline preserves both preprocessing and clustering steps, reducing the risk of inconsistent transformations between training and inference.

The model should be loaded only from a trusted source, and the deployment environment should use compatible library versions.

## Flask Web Application

The project integrates the exported pipeline into a Flask web application.

The application provides a web interface through which users can enter customer information and obtain a predicted cluster assignment.

### Application Workflow

```text
Customer Input
      |
      v
HTML Form
      |
      v
Flask Backend
      |
      v
Input Validation
      |
      v
Load Fitted Pipeline
      |
      v
StandardScaler
      |
      v
K-Means Prediction
      |
      v
Cluster Assignment
      |
      v
Display Result
```

### Main Application Steps

1. Load the serialized pipeline when the application starts.
2. Receive annual income and spending score from the form.
3. Validate the input values.
4. Create a DataFrame using the same feature names and order used during training.
5. Pass the input through the fitted pipeline.
6. Obtain the predicted cluster identifier.
7. Display the assigned cluster and its corresponding segment interpretation.

The model returns a cluster number rather than a supervised prediction such as a class probability. Cluster interpretation is added by mapping the cluster identifier to the segment descriptions established during analysis.

## Deployment on Vercel

The Flask application is configured for deployment on Vercel.

The deployment process generally involves:

1. Preparing the Flask application and its entry point.
2. Including the serialized pipeline in the deployment package or configuring a suitable way to access the artifact.
3. Creating a `requirements.txt` file with the required dependencies.
4. Configuring Vercel to recognize and run the Python application.
5. Deploying the project from the repository.
6. Testing the deployed application with valid customer inputs.

The deployed application should be tested to ensure that:

- The Flask backend starts correctly.
- The serialized model can be loaded.
- Input validation works as expected.
- Predictions are returned successfully.
- The frontend displays the resulting cluster.
- The application handles invalid inputs appropriately.

Vercel's Python runtime and deployment configuration may impose runtime and file-size constraints, so the final configuration should match the actual project setup.

## Running the Application Locally

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the dependencies listed in the project's `requirements.txt`:

```bash
pip install -r requirements.txt
```

Run the Flask application using the actual entry point in the repository. For example, if the entry point is `app.py`:

```bash
python app.py
```

Open the application at:

http://127.0.0.1:5000

The commands and paths should be adjusted if the Flask application uses a different directory structure or entry-point filename.

## Model Artifact

The exported pipeline is:

```text
complete_customer_segmentation_pipeline.pkl
```

It contains the fitted preprocessing and clustering components required to assign new customers to the learned clusters.

## Technologies Used

### Programming and Data Analysis

- Python
- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- StandardScaler
- K-Means Clustering
- Elbow Method
- Silhouette Score
- Scikit-Learn Pipeline

### Deployment

- Joblib or Pickle
- Flask
- HTML
- CSS
- Vercel

## Key Learning Outcomes

- Unsupervised machine learning
- Customer segmentation
- Exploratory Data Analysis
- Feature selection
- Feature scaling
- K-Means Clustering
- Cluster-centre interpretation
- Elbow Method
- Within-Cluster Sum of Squares (WCSS)
- Silhouette Score
- Clustering evaluation
- Scikit-learn pipelines
- Model serialization
- Loading saved models for inference
- Flask integration
- HTML form handling
- Model deployment on Vercel

---

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

- `movie_id`
- `title`
- `overview`
- `genres`
- `keywords`
- `cast`
- `crew`

## Recommendation Approach

The project uses **content-based filtering**.

Instead of using user ratings, recommendations are generated from the similarity between movie metadata.

The following information is used:

- Movie overview
- Genres
- Keywords
- Cast
- Director

These fields are combined into a single column:

```text
tags
```

## Data Preprocessing

The project performs:

1. Dataset merging.
2. Column selection.
3. Missing-value handling.
4. Duplicate checking.
5. Genre extraction.
6. Keyword extraction.
7. Cast extraction.
8. Director extraction.
9. Text normalization.
10. Creation of the `tags` column.

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
5. Returns the top five similar movies.

## Model Artifacts

The application uses the following serialized files:

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

Run the Flask application from the project root:

```bash
python backend/app.py
```

Open the application at:

http://127.0.0.1:5000

## Docker

Build the image:

```bash
docker build -t movies_recommender_system_project .
```

Run the container:

```bash
docker run -p 5000:5000 movies_recommender_system_project
```

Open the application at:

http://localhost:5000

## Project Structure

```text
MovieRecommenderSystem MLEngineering PROJECT/
├── backend/
│   └── app.py
├── frontend/
│   └── index.html
├── Dockerfile
├── requirements.txt
├── movies.pkl
├── similarity.pkl
├── movies_recommender_system.pkl
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── MOVIE RECOMMENDER SYSTEM (Content-Based).ipynb
├── MOVIE RECOMMENDER SYSTEM (Content-Based).pdf
└── README.md
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- CountVectorizer
- Cosine Similarity
- Flask
- HTML
- CSS
- Docker

## Key Learning Outcomes

- Content-based recommendation systems
- Text preprocessing
- Feature engineering
- Stemming
- Bag-of-Words
- CountVectorizer
- Cosine similarity
- Recommendation generation
- Model serialization
- Flask deployment
- Docker containerization

---

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
     EDA           Hypothesis Testing
      |                    |
      +---------+----------+
                |
                v
      Feature Engineering
                |
                v
        Traditional ML
          /         \
         v           v
    Regression   Classification
         |           |
         v           v
 Delivery Time   Price Segment
  Prediction      Prediction
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

- Area
- City
- Restaurant
- Price
- Average ratings
- Total ratings
- Address
- Food type
- Delivery time

## Exploratory Data Analysis

The project performs analysis of:

- Delivery-time distribution
- Restaurant prices
- Average ratings
- Total ratings
- Food types
- City-level patterns
- Relationships between price and ratings
- Relationships between ratings and delivery time

Visualizations are created using:

- Matplotlib
- Seaborn

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

Tests whether average delivery time differs among the following restaurant categories:

- Indian
- Chinese
- Fast Food

### Chi-Square Test

Tests the relationship between:

- City
- Food Type

The notebook uses a significance level of:

```python
alpha = 0.05
```

where applicable.

## Machine Learning

### 1. Delivery Time Prediction

The project predicts delivery time using restaurant, pricing, rating, and location information.

Regression algorithms compared include:

- Linear Regression
- K-Nearest Neighbors Regressor
- Decision Tree Regressor
- Extra Trees Regressor
- AdaBoost Regressor
- XGBoost Regressor

Models are evaluated using:

- R²
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The recorded notebook results identify XGBoost as the selected regression model, with an R² of approximately 0.67.

The trained model is stored as:

```text
Swiggy_FoodDeliveryTimePrediction_Model.pkl
```

### 2. Fast vs. Slow Delivery

A delivery-speed target is created using the median delivery time.

```text
Fast -> Delivery time <= median
Slow -> Delivery time > median
```

The project investigates relationships between delivery speed and:

- Price
- Average rating
- Total ratings

A Decision Tree Classifier is used for this task.

### 3. Premium vs. Budget

A price segment is created using restaurant price.

```text
Premium -> Price > 500
Budget  -> Price <= 500
```

The classification models are compared, and the trained model is exported as:

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

Example response:

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

Expected input fields include:

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

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install flask pandas numpy scikit-learn xgboost joblib
```

Run the application from the project root:

```bash
python backend/app.py
```

Open the application at:

http://127.0.0.1:5000

## Project Structure

```text
Swiggy FoodDelivery Analysis Website/
├── backend/
│   └── app.py
├── frontend/
│   └── index.html
├── dataset/
│   └── swiggy.csv
├── Price_Classification.pkl
├── Swiggy_FoodDeliveryTimePrediction_Model.pkl
├── source_code_swiggy.ipynb
├── source_code_swiggy.pdf
├── swiggy_fdAnalysis_project_demonstration.mp4
└── README.md
```

## Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

### Machine Learning

- Scikit-learn
- XGBoost

### Deployment

- Joblib
- Flask
- HTML
- CSS

## Key Learning Outcomes

- Exploratory Data Analysis
- Statistical hypothesis testing
- t-tests
- ANOVA
- Chi-Square testing
- Regression
- Classification
- Cross-validation
- Traditional machine learning
- Model comparison
- Model serialization
- Flask APIs
- Machine learning deployment

---

## Author

**Om Satyawan Pathak**

Email: [omsatyawanpathakgit@gmail.com](mailto:omsatyawanpathakgit@gmail.com)
