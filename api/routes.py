from fastapi import APIRouter

#from src.config import VERSION
from api.schemas import CustomerData
from src.predict import predict_churn

from src.config import (
    VERSION,
    MODEL_NAME,
    FEATURES,
    VALIDATION
)

router = APIRouter()


@router.get("/health")
def health():

    return {

        "status": "OK",

        "version": VERSION

    }

@router.get("/model-info")
def model_info():

    return {

        "model": MODEL_NAME,

        "version": VERSION,

        "features": FEATURES,

        "validation_metrics": VALIDATION

    }

@router.post("/predict")
def predict(customer: CustomerData):

    result = predict_churn(
        customer.model_dump()
    )

    return result