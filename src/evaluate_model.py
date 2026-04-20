import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report

# Paths
DATA_PATH = "data/creditcard.csv"   # change if needed
MODEL_PATH = "models/model.pkl"
SCALER_PATH = "models/scaler.pkl"


def evaluate():
    print("📥 Loading dataset...")
    data = pd.read_csv(DATA_PATH)

    if "Class" not in data.columns:
        raise Exception("Dataset must contain 'Class' column")

    X = data.drop("Class", axis=1)
    y = data["Class"]

    print("✂️ Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    print("📦 Loading model & scaler...")
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        raise Exception("Model not found. Train first!")

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    print("⚙️ Scaling test data...")
    X_test_scaled = scaler.transform(X_test)

    print("🔍 Predicting...")
    y_pred = model.predict(X_test_scaled)

    print("\n📊 Evaluation Results:\n")

    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall: {recall_score(y_test, y_pred):.4f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    evaluate()