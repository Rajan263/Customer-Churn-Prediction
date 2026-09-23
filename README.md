# 📊 Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to **churn** based on customer demographics, services, contract details, and billing information.
The project covers the complete ML workflow from **data preprocessing and exploratory data analysis to model training, evaluation, FastAPI deployment, Streamlit UI, and Docker containerization**.

---

## 🚀 Project Overview

Customer churn is an important business problem for subscription-based companies. Identifying customers who are likely to leave can help businesses understand customer behavior and take appropriate retention actions.

In this project, a Machine Learning classification pipeline is developed using the **IBM Telco Customer Churn dataset**.

The trained model is integrated into a REST API using **FastAPI** and connected to a **Streamlit** frontend for interactive predictions.

The API is also containerized using **Docker** and the Docker image is published to Docker Hub.

---

## 🎯 Objectives

* Analyze customer behavior and churn patterns.
* Clean and preprocess customer data.
* Perform exploratory data analysis.
* Build Machine Learning classification models.
* Compare model performance using multiple evaluation metrics.
* Perform cross-validation.
* Tune model hyperparameters.
* Save the complete preprocessing + ML pipeline.
* Build a REST API using FastAPI.
* Create an interactive Streamlit application.
* Containerize the API using Docker.
* Publish the Docker image to Docker Hub.

---

## 🗂️ Dataset

The project uses the **IBM Telco Customer Churn dataset**.

### Dataset Information

* **Original records:** 7,043
* **Original features:** 21
* **Final records after duplicate removal:** 7,021
* **Final features:** 20 after removing `customerID`
* **Target variable:** `Churn`

### Target Classes

| Churn | Meaning          |
| ----- | ---------------- |
| No    | Customer stayed  |
| Yes   | Customer churned |

The final dataset contained:

* **No Churn:** 5,164 customers
* **Churn:** 1,857 customers

The target distribution was approximately:

* **73.55% — No Churn**
* **26.45% — Churn**

Because the classes are not perfectly balanced, the project considers metrics such as **Precision, Recall, F1 Score, and ROC-AUC** instead of relying only on accuracy.

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Removed `customerID` because it does not provide useful predictive information.
* Converted `TotalCharges` from object/string to numeric.
* Handled blank values in `TotalCharges`.
* Removed duplicate records.
* Checked missing values.
* Separated numerical and categorical features.
* Applied median imputation to numerical features.
* Applied most-frequent imputation to categorical features.
* Applied `StandardScaler` to numerical features.
* Applied `OneHotEncoder` to categorical features.
* Used `ColumnTransformer` and `Pipeline` to combine preprocessing and modeling.

---

## 🔎 Exploratory Data Analysis

Several relationships between customer characteristics and churn were analyzed.

### Contract Type

Customers with month-to-month contracts showed a higher observed churn rate compared with customers on one-year and two-year contracts.

| Contract       | Churn Rate |
| -------------- | ---------: |
| Month-to-month |     42.64% |
| One year       |     11.27% |
| Two year       |      2.83% |

### Tenure

Average tenure differed substantially between churned and non-churned customers:

| Customer Group | Average Tenure |
| -------------- | -------------: |
| No Churn       |   37.64 months |
| Churn          |   18.09 months |

### Monthly Charges

| Customer Group | Average Monthly Charges |
| -------------- | ----------------------: |
| No Churn       |                   61.34 |
| Churn          |                   74.60 |

### Internet Service

The observed churn rates were:

| Internet Service    | Churn Rate |
| ------------------- | ---------: |
| DSL                 |     18.89% |
| Fiber optic         |     41.78% |
| No internet service |      7.21% |

### Payment Method

Electronic check customers had an observed churn rate of approximately **45.15%**, while the other payment methods had lower observed churn rates.

These findings represent **associations in the dataset and should not be interpreted as causal relationships**.

---

## 🤖 Machine Learning Models

The following classification models were explored:

### 1. Logistic Regression

Used as a baseline classification model.

### 2. Random Forest

Used to capture nonlinear relationships and interactions between features.

### 3. Gradient Boosting

Used as another tree-based classification approach.

---

## 🔄 Machine Learning Pipeline

The project uses Scikit-learn pipelines to ensure that preprocessing and model training are handled consistently.

```text
Raw Customer Data
       ↓
Train/Test Split
       ↓
ColumnTransformer
   ┌───────────────┐
   │               │
Numerical       Categorical
   │               │
Median           Most Frequent
Imputation       Imputation
   │               │
StandardScaler   OneHotEncoder
   │               │
   └───────┬───────┘
           ↓
       ML Model
           ↓
       Prediction
```

---

## 📈 Model Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix
* Classification Report
* Cross-validation

F1 score was also used during cross-validation and hyperparameter tuning because the churn classes are imbalanced.

---

## ⚙️ Hyperparameter Tuning

Random Forest hyperparameters were tuned using `GridSearchCV`.

Parameters explored included:

```python
{
    "model__n_estimators": [100, 200],
    "model__max_depth": [None, 10, 20],
    "model__min_samples_split": [2, 5],
    "model__min_samples_leaf": [1, 2]
}
```

The best estimator obtained from GridSearchCV was used for the final prediction pipeline.

---

## 💾 Model Saving

The complete trained pipeline, including preprocessing and the model, was saved using Joblib:

```python
joblib.dump(best_rf_model, "customer_churn_model.pkl")
```

This allows the same preprocessing steps used during training to be automatically applied when new customer data is sent to the API.

---

# 🌐 FastAPI

A REST API was developed using FastAPI.

### API Endpoints

### Home

```http
GET /
```

Returns:

```json
{
  "message": "Customer Churn Prediction API is running"
}
```

### Prediction

```http
POST /predict
```

The endpoint accepts customer information and returns the predicted churn class and churn probability.

Example response:

```json
{
  "prediction": "Churn",
  "churn_probability": 0.73
}
```

FastAPI also provides interactive API documentation through:

```text
/docs
```

---

# 🖥️ Streamlit Application

A Streamlit frontend was created to allow users to enter customer information through a graphical interface.

The application collects:

* Gender
* Senior Citizen status
* Partner
* Dependents
* Tenure
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

After clicking **Predict Churn**, the application sends the data to the FastAPI endpoint and displays:

* Churn prediction
* Churn probability

---

# 🐳 Docker

The FastAPI application is containerized using Docker.

### Build Docker Image

```bash
docker build -t customer-churn-api:latest .
```

### Run Container

```bash
docker run -p 8000:8000 customer-churn-api:latest
```

The API will then be available at:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

---

# 🐳 Docker Hub

Docker image:

**rajan263/customer-churn-api:latest**

Pull the image using:

```bash
docker pull rajan263/customer-churn-api:latest
```

Run it using:

```bash
docker run -p 8000:8000 rajan263/customer-churn-api:latest
```

---

# 📁 Project Structure

```text
customer-churn-prediction/
│
├── app/
│   ├── main.py
│   └── predict.py
│
├── models/
│   └── customer_churn_model.pkl
│
├── notebooks/
│   └── customer_churn.ipynb
│
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├── streamlit_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

```bash
cd customer-churn-prediction
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Start FastAPI

```bash
uvicorn app.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 5. Start Streamlit

Open another terminal and run:

```bash
streamlit run streamlit_app.py
```

The Streamlit application will open in your browser.

---

# 🏗️ System Architecture

```text
                  Customer
                     │
                     ▼
             Streamlit Frontend
                     │
                     │ HTTP POST
                     ▼
              FastAPI REST API
                     │
                     ▼
        Saved ML Pipeline (.pkl)
                     │
                     ▼
             Churn Prediction
                     │
             ┌───────┴───────┐
             ▼               ▼
          Churn           No Churn
             │               │
             └───────┬───────┘
                     ▼
              Probability
```

---

# 🛠️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Logistic Regression
* Random Forest
* Gradient Boosting
* GridSearchCV
* Cross-validation

### API

* FastAPI
* Pydantic
* Uvicorn

### Frontend

* Streamlit

### Model Serialization

* Joblib

### Deployment & DevOps

* Docker
* Docker Hub

### Development Tools

* Jupyter Notebook
* Git
* GitHub

---

# 🔮 Future Improvements

Possible future improvements include:

* MLflow experiment tracking
* Cloud deployment
* Automated CI/CD pipeline
* Model monitoring
* Model versioning
* Feature importance dashboard
* Improved probability calibration
* Integration with a production database
* Automated model retraining

---

# 📌 Key Learning Outcomes

Through this project, I practiced:

* Data cleaning
* Exploratory Data Analysis
* Feature preprocessing
* Classification algorithms
* Model evaluation
* Cross-validation
* Hyperparameter tuning
* Scikit-learn pipelines
* Model serialization
* REST API development
* FastAPI
* Streamlit
* Docker
* Docker Hub
* End-to-end ML application development

---

## 👨‍💻 Author

**Rajan Kumar**

B.Tech Computer Science & Engineering

GitHub: `https://github.com/Rajan263`

LinkedIn: `https://linkedin.com/in/rajan-kumar263`
