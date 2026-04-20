import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

print("Loading dataset...")

df = pd.read_csv("data/creditcard.csv")

X = df.drop("Class", axis=1)
y = df["Class"]

print("Handling class imbalance...")

# Balance dataset (IMPORTANT)
fraud = df[df["Class"] == 1]
normal = df[df["Class"] == 0].sample(len(fraud))

df_balanced = pd.concat([fraud, normal])

X = df_balanced.drop("Class", axis=1)
y = df_balanced["Class"]

print("Splitting data...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Scaling features...")

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print("Training model...")

model = RandomForestClassifier(
    n_estimators=200,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

print("Evaluating model...")

y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("Saving model...")

os.makedirs("models", exist_ok=True)

joblib.dump(model, "models/model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Training complete!")