# Customer Churn Prediction System

## Project Overview

This project is an end-to-end machine learning classification system that predicts whether a telecom customer is likely to churn.

The project covers the complete workflow from data inspection and preprocessing to model comparison, model export, and deployment through a Flask web application.

The final system allows a user to enter customer details through a web form. The Flask backend converts the entered values into a Pandas DataFrame, passes them to the trained machine learning pipeline, and displays whether the customer is predicted to churn or not.

---

## Problem Statement

Customer churn is a major business problem for subscription-based companies.

The objective of this project is to build a machine learning classification model that can identify customers who are likely to leave the telecom service based on their account, service, contract, and billing information.

The final application provides two possible predictions:

- Customer will churn
- Customer will not churn

---

## Project Objectives

The main objectives of this project are:

- Analyze and prepare the telecom customer churn dataset
- Handle categorical and numerical features
- Compare multiple machine learning classification algorithms
- Evaluate models using cross-validation
- Select the best-performing model
- Evaluate the final model on unseen test data
- Export the trained model using Joblib
- Build a Flask backend for prediction
- Build an HTML and CSS frontend
- Allow users to enter customer information through a web form
- Display the predicted churn result directly on the website

---

## Dataset

The project uses a telecom customer churn dataset containing customer account information, service usage information, billing information, and churn status.

The original dataset contains:

- 7,043 customer records
- 21 columns

After data preparation and removal of unusable records, the working dataset contains 7,032 records.

### Target Variable

The target column is:

```text
Churn
```

The original target values are:

```text
No
Yes
```

They are converted into:

```text
No  -> 0
Yes -> 1
```

where:

```text
0 = Customer will not churn
1 = Customer will churn
```

---

## Features Used for Machine Learning

The final model uses the following 13 customer features:

| Feature | Description |
|---|---|
| `gender` | Customer gender |
| `tenure` | Number of months the customer has stayed with the company |
| `Dependents` | Whether the customer has dependents |
| `SeniorCitizen` | Whether the customer is a senior citizen |
| `Partner` | Whether the customer has a partner |
| `InternetService` | Type of internet service |
| `PhoneService` | Whether the customer has phone service |
| `TechSupport` | Whether the customer has technical support |
| `Contract` | Customer contract type |
| `PaymentMethod` | Customer payment method |
| `TotalCharges` | Total amount charged to the customer |
| `StreamingTV` | Whether the customer uses streaming TV |
| `StreamingMovies` | Whether the customer uses streaming movies |

---

## Data Preparation

The following preprocessing steps are performed before model training:

### 1. Remove Customer ID

The `customerID` column is removed because it is an identifier and does not provide useful predictive information.

### 2. Standardize Service Categories

For selected service columns, values such as:

```text
No internet service
```

are converted to:

```text
No
```

### 3. Convert Total Charges

`TotalCharges` is converted to a numerical datatype.

Invalid values are converted to missing values and removed.

### 4. Encode the Target

The `Churn` target is converted from text labels to numerical labels.

### 5. Train-Test Split

The data is divided into training and testing datasets.

The project uses a stratified split so that the churn class distribution is maintained in both training and testing data.

### 6. Numerical Feature Processing

Numerical columns are processed using:

```text
StandardScaler
```

### 7. Categorical Feature Processing

Categorical columns are processed using:

```text
OneHotEncoder
```

Unknown categories are ignored during transformation.

---

## Machine Learning Pipeline

The preprocessing logic and machine learning model are combined into a single Scikit-learn/Imbalanced-learn pipeline.

This is useful because the exported model contains both:

```text
Raw Customer Data
        |
        v
ColumnTransformer
        |
        +-- Numerical Features -> StandardScaler
        |
        +-- Categorical Features -> OneHotEncoder
        |
        v
Classification Model
        |
        v
Churn Prediction
```

Because preprocessing is included inside the trained pipeline, the Flask application can directly pass raw customer input to the exported model.

---

## Machine Learning Algorithms Compared

The following classification algorithms were evaluated:

1. Logistic Regression
2. K-Nearest Neighbors Classifier
3. Extra Trees Classifier
4. AdaBoost Classifier
5. XGBoost Classifier

---

## Cross-Validation

The project uses:

```text
StratifiedKFold
```

with:

```text
3 folds
```

Stratified cross-validation is used because the churn dataset is imbalanced.

The models are compared using:

- Cross-validation accuracy
- Weighted F1 score

---

## Model Comparison

The obtained cross-validation results were:

| Model | CV Accuracy | CV Weighted F1 Score |
|---|---:|---:|
| Logistic Regression | 0.7984 | 0.7920 |
| Extra Trees | 0.7950 | 0.7866 |
| AdaBoost | 0.7829 | 0.7761 |
| KNN Classifier | 0.7780 | 0.7652 |
| XGBoost | 0.7737 | 0.7678 |

Based on cross-validation accuracy, Logistic Regression was selected as the best-performing model.

---

## Final Model Performance

The selected model was evaluated on the test dataset.

### Classification Report

| Class | Precision | Recall | F1 Score | Support |
|---|---:|---:|---:|---:|
| No Churn | 0.85 | 0.88 | 0.86 | 1033 |
| Churn | 0.63 | 0.55 | 0.59 | 374 |

Overall test accuracy:

```text
0.80
```

Weighted average F1 score:

```text
0.79
```

---

## Model Export

The trained pipeline is exported using Joblib:

```python
import joblib

joblib.dump(
    best_model,
    "CustomerChurnPredictionModel.pkl"
)
```

The generated file is:

```text
CustomerChurnPredictionModel.pkl
```

This file contains the trained machine learning pipeline used by the Flask application.

---

## Web Application

The machine learning model is integrated into a simple web application.

### Backend

The backend is built using:

```text
Flask
```

The Flask application:

1. Loads the exported machine learning model
2. Receives customer details from the HTML form
3. Converts the submitted values into a Pandas DataFrame
4. Sends the DataFrame to the trained model
5. Gets the churn prediction
6. Sends the prediction back to the webpage

### Frontend

The frontend is built using:

```text
HTML
CSS
```

No JavaScript framework is required.

The form provides structured inputs for customer information such as:

- Gender
- Partner status
- Dependents
- Senior citizen status
- Tenure
- Phone service
- Internet service
- Technical support
- Contract
- Payment method
- Total charges
- Streaming TV
- Streaming movies

The result is displayed on the same webpage after prediction.

---

## Project Architecture

```text
User
 |
 v
HTML/CSS Form
 |
 | POST Request
 v
Flask Backend
 |
 v
Pandas DataFrame
 |
 v
CustomerChurnPredictionModel.pkl
 |
 +-- StandardScaler
 |
 +-- OneHotEncoder
 |
 +-- Logistic Regression
 |
 v
Prediction
 |
 +-- 0 -> Customer will not churn
 |
 +-- 1 -> Customer will churn
 |
 v
Result displayed on webpage
```

---

## Project Structure

```text
Customer-Churn-Prediction/
|
|-- backend/
|   |-- app.py
|
|-- frontend/
|   |-- index.html
|
|-- CustomerChurnPredictionModel.pkl
|
|-- dataset.csv
|
|-- Final_Customer_Churn_Prediction_Classification.ipynb
|
|-- Final_Customer_Churn_Prediction_Classification.pdf
|
|-- README.md
```

Depending on your local file names, the notebook or PDF names may differ slightly.

---

## Backend Code Flow

The Flask application loads the trained model using:

```python
model = joblib.load(MODEL_PATH)
```

When a user submits the form, Flask receives the values using:

```python
request.form
```

The values are then converted into the same input structure used during model development:

```python
single_data = pd.DataFrame([{
    "gender": gender,
    "tenure": tenure,
    "Dependents": dependents,
    "SeniorCitizen": senior_citizen,
    "Partner": partner,
    "InternetService": internet_service,
    "PhoneService": phone_service,
    "TechSupport": tech_support,
    "Contract": contract,
    "PaymentMethod": payment_method,
    "TotalCharges": total_charges,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies
}])
```

The prediction is generated using:

```python
pred = model.predict(single_data)[0]
```

The output is converted into a user-friendly message:

```text
0 -> This customer will NOT churn.
1 -> This customer WILL churn.
```

---

## Example Input

A sample customer record can be:

```text
Gender: Male
Partner: No
Dependents: Yes
Senior Citizen: No
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

The model processes this record and returns the predicted churn class.

---

## Technologies Used

### Programming Language

```text
Python
```

### Data Processing

```text
Pandas
NumPy
```

### Machine Learning

```text
Scikit-learn
Imbalanced-learn
XGBoost
```

### Visualization

```text
Matplotlib
Seaborn
```

### Model Serialization

```text
Joblib
```

### Backend

```text
Flask
```

### Frontend

```text
HTML
CSS
```

---

## Python Libraries

The main libraries used in this project include:

```python
pandas
numpy
matplotlib
seaborn
scikit-learn
imbalanced-learn
xgboost
joblib
flask
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Move into the project folder:

```bash
cd Customer-Churn-Prediction
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install flask pandas numpy scikit-learn imbalanced-learn xgboost joblib matplotlib seaborn
```

---

## Running the Flask Application

From the project root directory, run:

```bash
python backend/app.py
```

After starting Flask, the terminal should display an address similar to:

```text
http://127.0.0.1:5000
```

Open the address in your browser.

---

## Using the Application

1. Start the Flask application.
2. Open the local Flask URL in your browser.
3. Fill in all customer details.
4. Click the prediction button.
5. The input values are sent to the Flask backend.
6. Flask passes the data to the trained machine learning pipeline.
7. The predicted churn result is displayed on the webpage.

---

## Important Input Categories

The categorical values submitted by the website should match the values used during model training.

### Gender

```text
Male
Female
```

### Partner

```text
Yes
No
```

### Dependents

```text
Yes
No
```

### Senior Citizen

```text
0
1
```

### Phone Service

```text
Yes
No
```

### Internet Service

```text
DSL
Fiber optic
No
```

### Tech Support

```text
Yes
No
```

### Contract

```text
Month-to-month
One year
Two year
```

### Payment Method

```text
Electronic check
Mailed check
Bank transfer (automatic)
Credit card (automatic)
```

### Streaming TV

```text
Yes
No
```

### Streaming Movies

```text
Yes
No
```

Using dropdown fields in the HTML form helps ensure that users submit valid categorical values.

---

## Why the Entire Pipeline Is Exported

A major advantage of this project is that the preprocessing steps are included inside the machine learning pipeline.

Without a pipeline, the web application would have to separately perform:

```text
Scaling
Encoding
Column transformations
Prediction
```

With the exported pipeline, the Flask application only needs to do:

```python
model.predict(single_data)
```

The pipeline automatically performs the required transformations before prediction.

This reduces preprocessing inconsistencies between the notebook and deployed application.

---

## Model Evaluation Techniques

The project includes multiple evaluation approaches.

### Cross-Validation

Used to compare multiple machine learning models more reliably.

### Accuracy

Measures the percentage of predictions classified correctly.

### Weighted F1 Score

Used alongside accuracy to evaluate classification performance while considering class frequencies.

### Confusion Matrix

Used to compare actual churn labels against predicted churn labels.

### Classification Report

Provides:

- Precision
- Recall
- F1 score
- Support

for both churn and non-churn customers.

---

## Business Use Case

A telecom company could use a churn prediction system to identify customers who may be at risk of leaving.

Predictions could support business activities such as:

- Customer retention analysis
- Identifying high-risk customer groups
- Prioritizing customers for retention campaigns
- Improving customer support strategies
- Reviewing contract and service-related churn patterns
- Supporting data-driven retention decisions

The model should be treated as a decision-support system rather than as a replacement for business judgment.

---

## Current Limitations

The current project has several limitations:

- Predictions depend on the quality and representativeness of the training dataset.
- The model predicts churn using only the selected 13 features.
- The churn class has lower recall than the non-churn class.
- The current web application is designed for individual customer predictions.
- The application does not currently store prediction history.
- The application does not currently provide user authentication.
- The application is intended as a machine learning portfolio project rather than a production telecom platform.

---

## Possible Future Improvements

Future versions of the project could include:

- Churn probability instead of only a binary prediction
- Batch prediction using CSV uploads
- Prediction history
- Database integration
- REST API endpoints
- Cloud deployment
- Docker support
- Model monitoring
- Data validation
- Automated retraining pipelines
- Improved class imbalance handling
- Additional feature engineering
- Hyperparameter optimization
- Explainable AI features
- Customer-level churn explanations
- Dashboard for churn analytics

---

## Key Learning Outcomes

This project demonstrates practical knowledge of:

- Data preprocessing
- Classification algorithms
- Handling categorical and numerical features
- Scikit-learn pipelines
- Cross-validation
- Imbalanced classification evaluation
- Model comparison
- Confusion matrix interpretation
- Classification reports
- Model serialization
- Flask backend development
- HTML form handling
- CSS-based frontend design
- Connecting a machine learning model to a web application
- Building an end-to-end machine learning project

---

## End-to-End Workflow

```text
Dataset
   |
   v
Data Inspection
   |
   v
Data Cleaning
   |
   v
Feature Selection
   |
   v
Train-Test Split
   |
   v
Preprocessing Pipeline
   |
   v
Train Multiple Models
   |
   v
Stratified Cross-Validation
   |
   v
Model Comparison
   |
   v
Select Best Model
   |
   v
Test Set Evaluation
   |
   v
Export Model
   |
   v
Flask Backend
   |
   v
HTML/CSS Frontend
   |
   v
User Input
   |
   v
Churn Prediction
```

---

## Conclusion

This project demonstrates an end-to-end customer churn prediction workflow using traditional machine learning.

Multiple classification algorithms are compared using stratified cross-validation, and the selected model is evaluated using classification metrics and a confusion matrix.

The complete preprocessing and prediction pipeline is exported using Joblib and integrated with a Flask backend. A responsive HTML and CSS frontend allows users to enter customer information and receive a churn prediction through a browser.

The project therefore combines data preprocessing, model development, model evaluation, model serialization, backend development, and frontend integration into one complete machine learning application.

---

## Author

Om Satyawan Pathak
