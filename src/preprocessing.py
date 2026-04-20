import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    """
    Load dataset from CSV file
    """
    data = pd.read_csv(file_path)
    return data


def preprocess_data(data):
    """
    Preprocess dataset:
    - Handle missing values
    - Split features and target
    - Scale features
    """

    # Check target column
    if "Class" not in data.columns:
        raise Exception("Dataset must contain 'Class' column")

    # Handle missing values (if any)
    data = data.dropna()

    # Split features & target
    X = data.drop("Class", axis=1)
    y = data["Class"]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler


def preprocess_input(input_data, scaler):
    """
    Preprocess new input data for prediction
    """
    input_scaled = scaler.transform(input_data)
    return input_scaled