import joblib
import pandas as pd

# Chargement du modèle sauvegardé
model = joblib.load("../model/modele_final_calibre.joblib")

client = {
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 5,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "Fiber optic",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "Yes",
    "StreamingMovies": "Yes",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 85.2,
    "TotalCharges": 425.8
}

df = pd.DataFrame([client])

prediction = model.predict(df)[0]
probability = model.predict_proba(df)[0, 1]

print("Prédiction :", prediction)
print("Probabilité :", round(probability, 4))