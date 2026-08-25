# Telco Customer Churn Prediction

## Description

Ce projet a été réalisé dans le cadre du cours d'Apprentissage Supervisé (M1 Data Science et Intelligence Artificielle).

L'objectif est de développer un système complet de prédiction du churn (résiliation) des clients d'un opérateur de télécommunications. Le projet couvre l'ensemble du cycle de vie d'un modèle de Machine Learning, depuis la préparation des données jusqu'au déploiement d'une API REST en passant par l'optimisation, la calibration et l'interprétabilité du modèle.

Le modèle final est une régression logistique optimisée avec **Optuna**, calibrée avec **CalibratedClassifierCV**, puis déployée à l'aide de **FastAPI**.

---

# Objectifs

Les principaux objectifs sont :

- analyser les données des clients ;
- construire un pipeline de prétraitement reproductible ;
- entraîner plusieurs modèles de classification ;
- optimiser les hyperparamètres avec Optuna ;
- calibrer les probabilités de churn ;
- interpréter les prédictions avec SHAP ;
- déployer le modèle sous forme d'API REST ;
- mettre en place des tests unitaires avec Pytest.

---

# Jeu de données

Le projet utilise le jeu de données **Telco Customer Churn**.

Chaque observation représente un client avec des informations concernant :

- les caractéristiques démographiques ;
- les services souscrits ;
- les modalités du contrat ;
- les informations de facturation.

La variable cible est :

**Churn**

- Yes : le client a résilié son abonnement ;
- No : le client est resté fidèle.

---

# Variables utilisées

Les principales variables utilisées sont :

- gender
- SeniorCitizen
- Partner
- Dependents
- tenure
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

---

# Modèle retenu

Le modèle final est une **Régression Logistique**.

Le pipeline comprend :

- imputation des valeurs manquantes ;
- standardisation des variables numériques ;
- encodage One-Hot des variables catégorielles ;
- optimisation des hyperparamètres avec Optuna ;
- calibration des probabilités avec Platt Scaling (`CalibratedClassifierCV`).

---

# Performances
## Performances du modèle

| Métrique | Valeur |
|-----------|:------:|
| Accuracy | 0.803 |
| Precision | 0.651 |
| Recall | 0.553 |
| F1-score (jeu de test) | 0.598 |
| ROC-AUC | 0.846 |
| F1-score après optimisation (CV) | **0.631** |
| Gain après optimisation | **+0.038** |
| Calibration | Platt Scaling |
| Interprétabilité | SHAP |
| Tests Pytest | **5 / 5 réussis** |a ensuite été optimisé et calibré afin d'améliorer la qualité des probabilités de churn.

---

# Structure du projet

```text
telco-churn-prediction/

├── api/
├── data/
├── model/
├── notebooks/
├── src/
├── tests/
├── README.md
├── MODEL_CARD.md
├── requirements.txt
└── .gitignore
```

---

# Installation

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activation sous Windows :

```bash
.venv\Scripts\activate
```

Installation des dépendances :

```bash
pip install -r requirements.txt
```

---

# Lancement de l'API

```bash
uvicorn api.main:app --reload
```

L'API est disponible à l'adresse :

```
http://127.0.0.1:8000
```

Documentation interactive :

```
http://127.0.0.1:8000/docs
```

---

# Endpoints disponibles

## GET /health

Retourne l'état de l'API.

## GET /model-info

Retourne :

- le modèle utilisé ;
- la version ;
- les variables attendues ;
- les performances de validation.

## POST /predict

Retourne :

- la prédiction du churn ;
- la probabilité de churn.

Exemple :

```json
{
  "prediction": "Yes",
  "probability": 0.7429
}
```

---

# Tests

Les tests unitaires ont été réalisés avec **Pytest**.

Ils vérifient :

- la structure de la réponse ;
- les probabilités ;
- la gestion des valeurs manquantes ;
- les variables attendues ;
- les performances sur un mini-jeu de référence.

Résultat :

```
=========================
5 tests réussis
=========================
```
(.venv) C:\telco-churn-prediction>pytest -v
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.14.2, pytest-9.1.1, pluggy-1.6.0 -- C:\telco-churn-prediction\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\telco-churn-prediction
configfile: pytest.ini
plugins: anyio-4.14.2, Faker-40.36.0
collected 5 items

tests/test_model.py::test_prediction_output PASSED                                                                                           [ 20%]
tests/test_model.py::test_probability_range PASSED                                                                                           [ 40%]
tests/test_model.py::test_missing_values PASSED                                                                                              [ 60%]
tests/test_model.py::test_expected_features PASSED                                                                                           [ 80%]
tests/test_model.py::test_reference_performance PASSED                                                                                       [100%]
---

# Sérialisation

Le pipeline final est sauvegardé avec **Joblib** :

```
model/modele_final_calibre.joblib
```

Le modèle est chargé automatiquement par l'API FastAPI afin de produire les prédictions.

---

# Technologies utilisées

- Python 3.14
- Scikit-learn
- Pandas
- NumPy
- Optuna
- SHAP
- Joblib
- FastAPI
- Uvicorn
- Pytest

---

# Tests de l'API avec cURL

Les endpoints de l'API ont été testés à l'aide de l'outil `curl`.

## Vérification de l'état de l'API

Commande :

```bash
curl http://127.0.0.1:8000/health
```

Réponse :

```json
{
  "status": "OK",
  "version": "1.0.0"
}
```

Cette réponse confirme que l'API est opérationnelle.

---

## Informations sur le modèle

Commande :

```bash
curl http://127.0.0.1:8000/model-info
```

Réponse :

```json
{
  "model": "Logistic Regression",
  "version": "1.0.0",
  "features": [
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
  ],
  "validation_metrics": {
    "Accuracy": 0.8026,
    "Recall": 0.5431,
    "F1-score": 0.593,
    "ROC-AUC": 0.8461
  }
}
```

Cette requête retourne les informations du modèle déployé, les variables attendues ainsi que les performances obtenues sur le jeu de validation.

---

## Prédiction du churn

Commande :

```bash
curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d "{\"gender\":\"Female\",\"SeniorCitizen\":0,\"Partner\":\"Yes\",\"Dependents\":\"No\",\"tenure\":5,\"PhoneService\":\"Yes\",\"MultipleLines\":\"No\",\"InternetService\":\"Fiber optic\",\"OnlineSecurity\":\"No\",\"OnlineBackup\":\"No\",\"DeviceProtection\":\"No\",\"TechSupport\":\"No\",\"StreamingTV\":\"Yes\",\"StreamingMovies\":\"No\",\"Contract\":\"Month-to-month\",\"PaperlessBilling\":\"Yes\",\"PaymentMethod\":\"Electronic check\",\"MonthlyCharges\":79.85,\"TotalCharges\":398.25}"
```

Réponse :

```json
{
  "prediction": "Yes",
  "probability": 0.715
}
```

Cette réponse indique que le modèle prédit que le client est susceptible de résilier son abonnement (**Churn = Yes**) avec une probabilité estimée de **71,5 %**.

# Auteur

Mamadou Saidou Keita

Master 1 Data Science et Intelligence Artificielle

ISI Dakar, Sénégal