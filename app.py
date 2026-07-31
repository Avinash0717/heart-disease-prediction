from flask import Flask, request, jsonify, render_template, redirect, url_for
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model/heart_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.form

    features = np.array([[
        float(data["age"]),
        float(data["sex"]),
        float(data["cp"]),
        float(data["trestbps"]),
        float(data["chol"]),
        float(data["fbs"]),
        float(data["restecg"]),
        float(data["thalach"]),
        float(data["exang"]),
        float(data["oldpeak"]),
        float(data["slope"]),
        float(data["ca"]),
        float(data["thal"])
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease"

    return render_template(
        "index.html",
        prediction=result
    )

if __name__ == "__main__":
    app.run(debug=True)