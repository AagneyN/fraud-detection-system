import os
import numpy as np
from flask import Flask, request, jsonify, send_from_directory
import joblib

app = Flask(__name__, static_folder="frontend", static_url_path="")

model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")


@app.route("/")
def serve_home():
    return send_from_directory("frontend", "index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)

        features_scaled = scaler.transform(features)

        prediction = model.predict(features_scaled)[0]
        probability = model.predict_proba(features_scaled)[0][1]

        return jsonify({
            "prediction": "Fraud Detected" if prediction == 1 else "Legitimate Transaction",
            "fraud_probability": round(probability * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)