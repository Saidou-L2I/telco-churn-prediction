from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Telco Churn Prediction API",
    description="API de prédiction du churn des clients",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Bienvenue sur l'API Telco Churn Prediction"
    }