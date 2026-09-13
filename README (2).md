# 🚀 CustomerIQ — Customer & Revenue Intelligence Platform

> **An end-to-end AI-powered platform for customer churn prediction, Customer Lifetime Value estimation, revenue-at-risk analysis, and actionable retention insights.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost-orange)](https://xgboost.readthedocs.io/)
[![SQL](https://img.shields.io/badge/Database-SQL-blue?logo=mysql)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)](https://powerbi.microsoft.com/)
[![Status](https://img.shields.io/badge/Status-Completed-success)]()

---

## 📌 Overview

**CustomerIQ** is an end-to-end **Customer & Revenue Intelligence Platform** designed to help businesses understand customer behavior, identify customers at risk of churn, estimate future customer value, and quantify potential revenue loss.

The platform combines:

* 📊 Data Analytics
* 🧹 Data Preprocessing
* 🤖 Machine Learning
* 🗄️ SQL Database
* ⚡ FastAPI
* 📈 Power BI
* 💡 Business Intelligence
* 🎯 Customer Retention Strategies

Instead of only predicting **"Which customers will churn?"**, CustomerIQ answers the more important business questions:

> **Who is likely to churn? Why might they churn? How much revenue is at risk? Which customers should the business prioritize?**

---

# 🎯 Business Problem

Customer churn can significantly impact recurring revenue and customer acquisition costs.

Traditional dashboards usually show historical metrics such as:

* Revenue
* Customers
* Churn rate
* Sales
* Profit

But historical reporting alone does not answer:

* Which customers are likely to leave?
* Which high-value customers are at risk?
* How much revenue could be lost?
* What factors are driving churn?
* Which customers should receive retention efforts first?

**CustomerIQ addresses these gaps using predictive analytics and machine learning.**

---

# 💡 Key Features

## 1. 🔴 Customer Churn Prediction

Predicts the probability that a customer will churn.

### Output

* Churn probability
* Churn prediction
* Customer risk category
* Risk prioritization

Example:

| Customer   | Churn Probability | Risk      |
| ---------- | ----------------: | --------- |
| Customer A |               87% | 🔴 High   |
| Customer B |               54% | 🟠 Medium |
| Customer C |               18% | 🟢 Low    |

---

## 2. 💰 Customer Lifetime Value (CLV)

Estimates the potential value of a customer over their relationship with the business.

CLV helps identify:

* High-value customers
* Low-value customers
* Customers worth retaining
* Revenue contribution by customer segment

---

## 3. ⚠️ Revenue at Risk

Combines customer churn probability with customer value to estimate potential revenue exposure.

A simplified approach:

```text
Revenue at Risk
= Customer Value × Churn Probability
```

This allows businesses to focus retention efforts on customers who represent the greatest financial risk.

---

## 4. 📊 Customer Segmentation

Customers can be categorized into meaningful groups such as:

* 🟢 Low Risk
* 🟡 Medium Risk
* 🔴 High Risk
* 💎 High-Value Customers
* ⚠️ High-Value + High-Risk Customers

This enables targeted customer retention strategies.

---

## 5. 🧠 Executive Summary

The platform converts analytical results into business-friendly KPIs.

### Example Executive KPIs

* 👥 Total Customers
* 📉 Churn Rate
* 💰 Total Customer Lifetime Value
* ⚠️ Revenue at Risk
* 🔴 High-Risk Customers
* 💎 High-Value Customers

The goal is to allow management to understand the business situation quickly without going through raw datasets.

---

# 🏗️ System Architecture

```text
                 ┌─────────────────────┐
                 │     Raw Dataset     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Data Preprocessing  │
                 │ Cleaning & Feature   │
                 │ Engineering         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   SQL Database      │
                 └──────────┬──────────┘
                            │
             ┌──────────────┴──────────────┐
             │                             │
             ▼                             ▼
    ┌──────────────────┐          ┌─────────────────┐
    │ Machine Learning │          │   Power BI      │
    │                  │          │   Dashboard     │
    │ Churn Prediction │          │                 │
    │ CLV Prediction   │          │ Executive KPIs  │
    │ Risk Analysis    │          │ Revenue Risk    │
    └────────┬─────────┘          └─────────────────┘
             │
             ▼
    ┌──────────────────────┐
    │      FastAPI         │
    │      REST API        │
    └──────────┬───────────┘
               │
               ▼
    ┌──────────────────────┐
    │      Frontend        │
    │ Customer Intelligence│
    │       Interface      │
    └──────────────────────┘
```

---

# 🛠️ Tech Stack

| Category         | Technologies           |
| ---------------- | ---------------------- |
| Programming      | Python                 |
| Data Processing  | Pandas, NumPy          |
| Machine Learning | Scikit-learn, XGBoost  |
| Backend          | FastAPI                |
| Database         | SQL                    |
| Visualization    | Power BI, Matplotlib   |
| Frontend         | HTML, CSS, JavaScript  |
| API Testing      | Swagger / FastAPI Docs |
| Version Control  | Git & GitHub           |

---

# 📂 Project Structure

```text
CustomerIQ/
│
├── backend/
│   ├── ...
│   └── FastAPI application
│
├── frontend/
│   ├── ...
│   └── User interface
│
├── ml/
│   ├── ...
│   └── Machine learning models
│
├── CustomerIQ_Complete_Report.md
├── check_db.py
├── fix_width.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🤖 Machine Learning Workflow

The ML pipeline follows a standard end-to-end workflow:

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Train / Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Prediction
   ↓
Business Risk Analysis
```

### Model Evaluation

For churn prediction, the project focuses on classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

For business applications, **Recall and ROC-AUC** are particularly useful because missing a high-risk customer can result in potential revenue loss.

---

# 🔌 FastAPI

The backend exposes machine-learning functionality through REST APIs.

Example workflow:

```text
Frontend
   │
   │ Customer Information
   ▼
FastAPI
   │
   ▼
ML Model
   │
   ▼
Prediction
   │
   ▼
Risk Score + Business Insights
```

FastAPI also provides automatic interactive API documentation through Swagger UI.

---

# 📊 Power BI Dashboard

The Power BI dashboard provides an executive-level view of customer and revenue performance.

### Key Dashboard Components

#### KPI Cards

* Total Customers
* Total Churn Rate
* Total CLV
* Revenue at Risk

#### Visualizations

* Revenue at Risk by Region
* Churn Distribution
* Customer Risk Segmentation
* Customer Lifetime Value
* High-Risk Customer Analysis
* Revenue Contribution
* Customer Trends

The dashboard is designed to help decision-makers quickly identify areas requiring attention.

---

# 📈 Business Insights

CustomerIQ transforms predictions into actionable business insights.

### Example

Instead of:

> "Customer has an 82% probability of churn."

The platform can provide:

> **High-risk customer with significant potential revenue impact. Prioritize for retention outreach.**

This makes the project more useful from a **business analyst / data scientist perspective**.

---

# 🎯 Customer Retention Strategy

Based on customer risk and value:

| Customer Segment       | Recommended Action           |
| ---------------------- | ---------------------------- |
| High Risk + High Value | Immediate retention campaign |
| High Risk + Low Value  | Automated engagement         |
| Low Risk + High Value  | Loyalty / upselling          |
| Low Risk + Low Value   | Standard communication       |
| Medium Risk            | Monitor behavior             |

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/palakgupta29/custom.git
cd custom
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

## Start the Backend

Navigate to the backend directory:

```bash
cd backend
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Example Prediction Flow

```text
Customer Data
      ↓
API Request
      ↓
Feature Processing
      ↓
ML Model
      ↓
Churn Probability
      ↓
Customer Risk Score
      ↓
Revenue Impact
      ↓
Retention Recommendation
```

---

# 📊 Project Outcomes

CustomerIQ demonstrates the complete lifecycle of a modern data science application:

### Data

* Data cleaning
* Data transformation
* Exploratory analysis
* Feature engineering

### Analytics

* Customer analysis
* Revenue analysis
* Segmentation
* KPI development

### Machine Learning

* Predictive modeling
* Churn prediction
* Customer value estimation
* Risk scoring

### Engineering

* SQL database
* REST API
* Backend integration
* Frontend integration

### Business Intelligence

* Executive dashboard
* Revenue-at-risk analysis
* Customer prioritization
* Actionable recommendations

---

# 🌟 Why This Project?

Most beginner ML projects stop at:

```text
Dataset → Model → Accuracy
```

CustomerIQ goes further:

```text
Data
 ↓
Analytics
 ↓
Machine Learning
 ↓
API
 ↓
Dashboard
 ↓
Business Intelligence
 ↓
Actionable Decision
```

This makes it a practical **end-to-end Data Science + Analytics project** rather than just a machine learning notebook.

---

# 🚀 Future Enhancements

Planned improvements include:

* [ ] Automated model retraining
* [ ] Real-time churn prediction
* [ ] Customer recommendation engine
* [ ] Automated retention campaigns
* [ ] Email alerts for high-risk customers
* [ ] SHAP-based model explainability
* [ ] Advanced customer segmentation
* [ ] Cloud deployment
* [ ] CI/CD pipeline
* [ ] Automated data ingestion
* [ ] AI-generated executive summaries

---

# 👩‍💻 Author

### Palak Gupta

**B.Tech Data Science Student | Data Science | Data Analytics | Machine Learning**

I enjoy building end-to-end data solutions that combine **analytics, machine learning, APIs, databases, and business intelligence** to solve real-world problems.

### Connect With Me

* 💻 GitHub: [Palak Gupta](https://github.com/palakgupta29)

---

# ⭐ If You Like This Project

If you find **CustomerIQ** useful or interesting:

⭐ Star the repository
🍴 Fork the project
🐛 Open an issue
💡 Suggest an improvement

---

## 📜 License

This project is intended for educational and portfolio purposes.
