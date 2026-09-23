import joblib
import pandas as pd
from pathlib import Path


# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Model path
MODEL_PATH = BASE_DIR / "models" / "customer_churn_model.pkl"

# Load trained model
model = joblib.load(MODEL_PATH)


def predict_churn(customer_data):

    # Convert dictionary into DataFrame
    input_df = pd.DataFrame([customer_data])

    # Make prediction
    prediction = model.predict(input_df)[0]

    # Get churn probability
    probability = model.predict_proba(input_df)[0][1]

    # Convert prediction into readable output
    if prediction == 1:
        result = "Churn"
    else:
        result = "No Churn"

    return {
        "prediction": result,
        "churn_probability": round(float(probability), 4)
    }