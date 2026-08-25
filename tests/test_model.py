from fastapi.testclient import TestClient
from sklearn.metrics import accuracy_score

##############
import pandas as pd
##################################
from api.main import app

client = TestClient(app)


# ==============================
# Données de test
# ==============================

sample_customer = {
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


# ==========================================================
# Test 1 : La sortie possède la bonne structure
# ==========================================================

def test_prediction_output():

    response = client.post(
        "/predict",
        json=sample_customer
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "probability" in data

    assert isinstance(data["prediction"], str)
    assert isinstance(data["probability"], float)


# ==========================================================
# Test 2 : La probabilité est comprise entre 0 et 1
# ==========================================================

def test_probability_range():

    response = client.post(
        "/predict",
        json=sample_customer
    )

    probability = response.json()["probability"]

    assert 0 <= probability <= 1


# ==========================================================
# Test 3 : Gestion des valeurs manquantes
# ==========================================================

"""def test_missing_values():

    customer = sample_customer.copy()

    customer["TotalCharges"] = None

    response = client.post(
        "/predict",
        json=customer
    )

    assert response.status_code == 200"""
def test_missing_values():

    customer = sample_customer.copy()

    customer["TotalCharges"] = None

    response = client.post(
        "/predict",
        json=customer
    )

    print(response.json())   # <-- important

    assert response.status_code == 200


# ==========================================================
# Test 4 : Vérification des variables attendues
# ==========================================================

def test_expected_features():

    response = client.get("/model-info")

    assert response.status_code == 200

    features = response.json()["features"]

    expected_features = [
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

    assert features == expected_features


# ==========================================================
# Test 5 : Performance sur un mini jeu de référence
# ==========================================================
def test_reference_performance():

    # Chargement du mini jeu de référence
    X = pd.read_csv("data/raw/mini_X_test.csv")
    y = pd.read_csv("data/raw/mini_y_test.csv").squeeze()

    y_pred = []

    # Prédictions via l'API
    for _, row in X.iterrows():

        response = client.post(
            "/predict",
            json=row.to_dict()
        )

        assert response.status_code == 200

        y_pred.append(
            response.json()["prediction"]
        )

    # Calcul de la performance
    accuracy = accuracy_score(
        y,
        y_pred
    )

    # Vérification
    assert accuracy >= 0.70