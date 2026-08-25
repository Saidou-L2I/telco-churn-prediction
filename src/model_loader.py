import joblib

from src.config import MODEL_PATH


def load_model():
    """
    Charge le modèle sauvegardé.
    """

    return joblib.load(MODEL_PATH)


# Chargement unique du modèle
model = load_model()