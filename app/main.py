from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

from app.predict import predict_churn


app = FastAPI(
    title="Customer Churn Prediction API",
    description="API for predicting customer churn",
    version="1.0.0"
)


class CustomerData(BaseModel):

    gender: Literal["Male", "Female"]

    SeniorCitizen: int

    Partner: Literal["Yes", "No"]

    Dependents: Literal["Yes", "No"]

    tenure: int

    PhoneService: Literal["Yes", "No"]

    MultipleLines: Literal[
        "Yes",
        "No",
        "No phone service"
    ]

    InternetService: Literal[
        "DSL",
        "Fiber optic",
        "No"
    ]

    OnlineSecurity: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    OnlineBackup: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    DeviceProtection: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    TechSupport: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    StreamingTV: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    StreamingMovies: Literal[
        "Yes",
        "No",
        "No internet service"
    ]

    Contract: Literal[
        "Month-to-month",
        "One year",
        "Two year"
    ]

    PaperlessBilling: Literal["Yes", "No"]

    PaymentMethod: Literal[
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]

    MonthlyCharges: float

    TotalCharges: float


@app.get("/")
def home():

    return {
        "message": "Customer Churn Prediction API is running"
    }


@app.post("/predict")
def predict(customer: CustomerData):

    customer_dict = customer.model_dump()

    result = predict_churn(customer_dict)

    return result