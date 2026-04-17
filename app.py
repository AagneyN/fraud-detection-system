from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from src.predict import predict_transaction

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Fraud Detection API Running"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = data["features"]

    prediction, probability = predict_transaction(features)

    if prediction == 1:
        result = "Fraud Transaction"
    else:
        result = "Legitimate Transaction"

    return jsonify({
        "prediction": result,
        "fraud_probability": round(probability * 100, 2)
    })



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)