import random

def predict_transaction(features):
    prediction = random.choice([0, 1])
    probability = random.uniform(0.5, 0.99)
    return prediction, probability