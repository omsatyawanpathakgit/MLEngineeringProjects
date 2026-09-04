from flask import Flask, render_template, request
import pandas as pd
import joblib
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "frontend")
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "CustomerChurnPredictionModel.pkl"
)

model = joblib.load(MODEL_PATH)


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None

    if request.method == "POST":

        single_data = pd.DataFrame([{

            "gender": request.form["gender"],

            "Partner": request.form["Partner"],

            "Dependents": request.form["Dependents"],

            "SeniorCitizen": int(
                request.form["SeniorCitizen"]
            ),

            "tenure": int(
                request.form["tenure"]
            ),

            "PhoneService": request.form["PhoneService"],

            "InternetService": request.form["InternetService"],

            "TechSupport": request.form["TechSupport"],

            "Contract": request.form["Contract"],

            "PaymentMethod": request.form["PaymentMethod"],

            "TotalCharges": float(
                request.form["TotalCharges"]
            ),

            "StreamingTV": request.form["StreamingTV"],

            "StreamingMovies": request.form["StreamingMovies"]

        }])

        pred = model.predict(single_data)[0]

        if pred == 0:
            prediction = "This customer will NOT churn."
        else:
            prediction = "This customer WILL churn."

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)