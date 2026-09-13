# 🧠 CustomerIQ — Complete Project Report
### Customer Retention & Sales Intelligence Platform
**Presentation & Interview Preparation Guide**

---

## 🎯 1. BUSINESS PROBLEM & OBJECTIVE

### 💔 THE CORE PROBLEM
> **"Company ko pata tab chalta hai ki customer ja raha hai, jab woh ja CHUKA hota hai."**
Yeh **Reactive approach** hai — aur tab tak bahut der ho chuki hoti hai.

**Real-World Business Pain Points:**
1. **Customer Churn:** Naya customer lana 5x zyada mehenga hai existing ko rokne se.
2. **No Prioritization:** 1000 customers mein se kisko retain karein? Kisko call karein? (Random guessing)
3. **Revenue Risk Unknown:** "Kitna paisa dub sakta hai?" iska koi data-driven answer nahi hota.
4. **Regional Blind Spots:** Kis region mein churn zyada hai, pata nahi chalta.

### ✅ WHAT CustomerIQ SOLVES (The Objective)
| Business Problem | CustomerIQ ka Solution |
|---|---|
| "Kaunsa customer jayega?" | Churn Probability % predict karta hai |
| "Kitna valuable customer hai?" | CLV (Customer Lifetime Value) nikalta hai |
| "Kitna paisa risk mein hai?" | Revenue at Risk (Churn% × CLV) calculate karta hai |
| "Kahan focus karein?" | Regional heatmap and high-risk customer lists |

**Core Goals:**
1. **PREDICT:** Har customer ka churn probability predict karo BEFORE woh actually churn kare.
2. **QUANTIFY:** Revenue at Risk calculate karke exact financial impact batao.
3. **PRIORITIZE:** High-risk + High-value customers ko identify karo taaki sales team action le sake.

---

## 📌 2. PROJECT OVERVIEW (30-Second Elevator Pitch)

> **"CustomerIQ ek AI-powered business intelligence dashboard hai jo companies ko predict karne mein help karta hai ki kaunsa customer churn (leave) kar sakta hai, uski lifetime value kitni hai, aur agle mahine product sales kitna hoga — sab kuch real-time mein."**

**Solution:**
Ek complete ML + Dashboard platform jo:
- Customer churn predict karta hai
- CLV calculate karta hai
- Revenue at risk dikhata hai
- Regional sales analytics provide karta hai

---

## 🏗️ 3. SYSTEM ARCHITECTURE

```
┌─────────────────────────────────────────────────────┐
│              FRONTEND LAYER                         │
│         Streamlit Dashboard (Port 8501)             │
│  • Executive Summary  • Regional Analysis           │
│  • Customer Explorer  • ML Predictor                │
└──────────────────┬──────────────────────────────────┘
                   │ HTTP REST API calls (requests lib)
                   ▼
┌─────────────────────────────────────────────────────┐
│              BACKEND LAYER                          │
│         FastAPI Server (Port 8000)                  │
│  POST /api/predict   GET /api/summary               │
│  GET /api/region_analysis   GET /docs (Swagger)     │
└──────────┬──────────────────────┬───────────────────┘
           │                      │
           ▼                      ▼
┌─────────────────┐    ┌──────────────────────────┐
│   SQLite DB     │    │    ML Models (.pkl)       │
│  customers.db   │    │  churn_model.pkl (3.3MB)  │
│  1000 customers │    │  clv_model.pkl (7MB)      │
│  12 columns     │    │  sales_model.pkl (7MB)    │
└─────────────────┘    └──────────────────────────┘
```

**Data Flow:**
1. `synthetic_data.py` → 1000 customer records generate karta hai → `customers.db` mein save
2. `train.py` → DB se data read → 3 ML models train → `.pkl` files save
3. `backend/app.py` → models load → REST API expose karta hai
4. `frontend/dashboard.py` → DB directly read (charts ke liye) + API call (prediction ke liye)

---

## 💻 4. TECH STACK — DETAIL MEIN

### Frontend
- **Streamlit** (Python web UI)
- **Plotly Express & Graph Objects** (Charts)
- **Custom CSS** (Dark glassmorphism theme)

### Backend
- **FastAPI** (REST API)
- **Uvicorn** (Server)
- **Pydantic** (Validation)

### Machine Learning
- **Scikit-learn**
- **RandomForestClassifier** (Churn prediction)
- **RandomForestRegressor** (CLV & Sales prediction)
- **OneHotEncoder & ColumnTransformer** (Preprocessing)
- **Pipeline** (Preprocessing + Model wrapper)
- **Joblib** (Model save/load)

### Database & Utilities
- **SQLite** (Database)
- **Pandas & NumPy** (Data processing)
- **Requests** (API calls)

---

## 🗄️ 5. DATABASE SCHEMA (`customer_data`)

| Column | Type | Description |
|---|---|---|
| `customer_id` | INT | Unique customer identifier |
| `age` | INT | Customer age (18–70) |
| `tenure_months` | INT | Months with company (1–72) |
| `region` | TEXT | North / South / East / West |
| `product_category` | TEXT | Electronics / Software / Services / Hardware |
| `monthly_charges` | FLOAT | Monthly billing amount |
| `total_charges` | FLOAT | monthly_charges × tenure_months |
| `churn_prob_actual` | FLOAT | True churn probability (0–1) |
| `churned` | INT | 0 = Retained, 1 = Churned |
| `clv` | FLOAT | Customer Lifetime Value ($) |
| `revenue_at_risk` | FLOAT | churn_prob × CLV |
| `product_sales` | FLOAT | Next month expected sales volume |

---

## 🤖 6. MACHINE LEARNING — DETAIL MEIN

### Models
1. **Churn Prediction:** RandomForestClassifier (Output: 0 or 1, Probability 0-1) - ~92% Accuracy
2. **CLV Prediction:** RandomForestRegressor (Output: $ Value) - ~89% Accuracy
3. **Product Sales Prediction:** RandomForestRegressor (Output: Sales Volume) - ~87% Accuracy

### Preprocessing Pipeline
Input Data → ColumnTransformer (Numeric: passthrough, Categorical: OneHotEncoder) → RandomForest Model

---

## 🌐 7. BACKEND API

**Base URL:** `http://127.0.0.1:8000`

- `GET /`: Status check
- `POST /api/predict`: ML prediction via JSON request
- `GET /api/summary`: Top level stats
- `GET /api/region_analysis`: Regional breakdown
- `GET /docs`: Swagger documentation

---

## 🎨 8. FRONTEND — 4 TABS DETAIL

1. **📊 Executive Summary:** KPIs, Donut chart (Churn), Bubble chart (CLV vs Risk), Top 10 at-risk customers.
2. **🌍 Regional Analysis:** Region filters, Stacked bar chart, Heatmap (Sales by Region x Product).
3. **👥 Customer Explorer:** Advanced filtering (Region, Category, Status, Age), datatable, CSV download.
4. **🔮 ML Predictor:** Input form for new/existing customer → Shows Churn Prob (gauge chart), predicted CLV, and Risk.

---

## ▶️ 9. HOW TO RUN

```bash
# Terminal 1: Backend
cd c:\Users\palak\custom
uvicorn backend.app:app --reload --port 8000

# Terminal 2: Frontend
cd c:\Users\palak\custom
streamlit run frontend/dashboard.py
```

---

## ❓ 10. EXPECTED INTERVIEW QUESTIONS & ANSWERS

**Q1: Is project ka main purpose kya hai?**
> CustomerIQ ek business intelligence platform hai jo companies ko customer churn predict karne, lifetime value calculate karne, aur revenue at risk identify karne mein help karta hai.

**Q2: Tumne ye project kyun banaya?**
> Reactive approach ko pro-active banane ke liye. Agar pehle se pata chal jaye ki kaunsa customer jayega, toh company usse retain karne ke liye action le sakti hai.

**Q3: Churn model kaise kaam karta hai?**
> Churn model ek **RandomForestClassifier** hai. Input features hain: age, tenure_months, monthly_charges, total_charges, region, aur product_category. Output ek probability hoti hai (0 to 1). Accuracy ~92% hai.

**Q4: Revenue at Risk kaise calculate hota hai?**
> Revenue at Risk = Churn Probability × Customer Lifetime Value.

**Q5: Frontend backend se kaise communicate karta hai?**
> Streamlit Python ke `requests` library use karke FastAPI backend ko HTTP POST/GET call karta hai (`http://127.0.0.1:8000/api/...`).

**Q6: FastAPI kyun choose kiya, Flask kyun nahi?**
> Auto Swagger docs, Pydantic validation (automatic request checking), and high performance.

**Q7: Pipeline ka kya role hai?**
> Scikit-learn Pipeline preprocessing (OneHotEncoding) aur model ko ek unit mein wrap karta hai taaki data leakage na ho aur code clean rahe.

**Q8: Streamlit mein `unsafe_allow_html=True` kyun use kiya?**
> Custom CSS (glassmorphism theme, gradients) aur custom HTML KPI cards banane ke liye, kyunki Streamlit default components limited hote hain.

---

## 🎯 11. PRESENTATION FLOW (Kal ke liye Script)

**Opening (30 sec):**
> "Main aaj CustomerIQ present karne ja raha/rahi hoon — yeh ek AI-powered customer intelligence platform hai jo predict karta hai ki kaunsa customer company chhod sakta hai aur kitna revenue at risk hai."

**Problem (1 min):**
> "Customer churn ek silent revenue killer hai. Jab tak company ko pata chalta hai ki customer ja raha hai, tab tak woh ja chuka hota hai. Hum is problem ko proactively solve karte hain."

**Architecture (2 min):**
> "Project mein 3 layers hain — Streamlit frontend, FastAPI backend, aur SQLite database with 3 trained ML models."

**Live Demo (3-4 min):**
1. Executive Summary tab kholo → KPI cards dikhao
2. Regional Analysis → Heatmap dikhao
3. Customer Explorer → Filter karke CSV download karo
4. ML Predictor → Ek customer ka data fill karke predict karo

**Closing (30 sec):**
> "Future improvements mein XGBoost models, real CRM integration, aur Docker deployment planned hai."
