import pandas as pd

from src.model_loader import model


def predict_churn(data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]

    probability = float(
        model.predict_proba(df)[0, 1]
    )

    return {
        "prediction": prediction,
        "probability": round(probability, 4)
    }