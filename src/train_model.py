import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

from src.preprocessing import load_data, preprocess_data


def train():

    df = load_data("data/creditcard.csv")

    X_train, X_test, y_train, y_test = preprocess_data(df)

    models = {

        "Logistic Regression": LogisticRegression(max_iter=1000),

        "Decision Tree": DecisionTreeClassifier(),

        "Random Forest": RandomForestClassifier(n_estimators=100),

        "XGBoost": XGBClassifier()

    }

    trained_models = {}

    for name, model in models.items():

        print("Training", name)

        model.fit(X_train, y_train)

        trained_models[name] = model

    best_model = trained_models["Random Forest"]

    joblib.dump(best_model, "models/fraud_model.pkl")

    print("Model saved successfully!")


if __name__ == "__main__":
    train()