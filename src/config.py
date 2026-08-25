from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "modele_final_calibre.joblib"

MODEL_NAME = "Logistic Regression"

VERSION = "1.0.0"

AUTHOR = "Mamadou Saidou Keita"

FEATURES = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges"
]

VALIDATION = {
    "Accuracy": 0.8026,
    "Recall": 0.5431,
    "F1-score": 0.5930,
    "ROC-AUC": 0.8461
}