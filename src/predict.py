import os
import numpy as np
import joblib

# Paths
MODEL_PATH = "models/model.pkl"
SCALER_PATH = "models/scaler.pkl"


def load_model():
    """
    Load trained model and scaler
    """
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise Exception("Model or scaler not found. Train the model first.")

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return model, scaler


def predict_transaction(features):
    """
    Predict whether a transaction is fraud or not

    Parameters:
    features (list or array): input features

    Returns:
    int: 0 (Legitimate) or 1 (Fraud)
    """

    model, scaler = load_model()

    # Convert input to numpy array
    features = np.array(features).reshape(1, -1)

    # Scale input
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)[0]

    return int(prediction)


# 🔹 Test this file directly
if __name__ == "__main__":
    # Example dummy input (must match number of features in dataset)
    sample_input = [0.1] * 30   # adjust based on your dataset columns

    result = predict_transaction(sample_input)

    if result == 1:
        print("🚨 Fraud Detected")
    else:
        print("✅ Legitimate Transaction")