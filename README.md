

# 🚀 Modern Data Stack Project

## 📌 Overview

This project implements a **Modern Data Stack** using:

* 🐍 Python
* 🐘 PostgreSQL
* 🧱 dbt (Data Build Tool)
* 📊 Apache Superset
* 📈 Power BI
* 🔄 Prefect

The goal of this project is to demonstrate a complete **data pipeline architecture** from raw data ingestion to business intelligence dashboards.

---

## 🏗 Architecture

```
        Source Data (CSV / API / App)
                   │
                   ▼
              Python (ETL)
                   │
                   ▼
              PostgreSQL (Raw)
                   │
                   ▼
              dbt (Transformations)
                   │
                   ▼
          Analytics Layer (Mart Tables)
               │                │
               ▼                ▼
        Apache Superset      Power BI
                   ▲
                   │
               Prefect
           (Orchestration)
```

---

## 🧩 Tech Stack

### 🐍 Python

Used for:

* Data ingestion (CSV / API)
* Data cleaning
* Initial validation
* Loading data into PostgreSQL

Libraries example:

* pandas
* sqlalchemy
* psycopg2

---

### 🐘 PostgreSQL

Relational database used as:

* Raw data storage (bronze layer)
* Staging & transformed layers
* Data warehouse foundation

---

### 🧱 dbt

Used for:

* Data transformation
* Creating staging models
* Building marts (fact & dimension tables)
* Testing data quality
* Documentation

Layers:

* `raw`
* `staging`
* `mart`

---

### 🔄 Prefect

Workflow orchestration:

* Schedule pipelines
* Automate dbt runs
* Monitor data jobs
* Handle failures & retries

---

### 📊 Apache Superset

Used for:

* Exploratory data analysis
* SQL Lab
* Interactive dashboards

---

### 📈 Power BI

Used for:

* Business reporting
* Executive dashboards
* KPI monitoring

---

## 📂 Project Structure

```
data-stack-project/
│
├── data/                  # Raw CSV files
├── ingestion/             # Python scripts
├── dbt_project/           # dbt models
│   ├── models/
│   │   ├── staging/
│   │   ├── marts/
│   │   └── sources.yml
│
├── prefect_flows/         # Prefect pipelines
├── dashboards/
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/iy-fadili/FADILI-AHMED.git
cd data-stack
```

---

### 2️⃣ Setup Python environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

---

### 3️⃣ Setup PostgreSQL

Create a database:

```sql
CREATE DATABASE clinic_db;
```

Update connection settings in:

* dbt `profiles.yml`
* Python config file

---

### 4️⃣ Run ingestion

```bash
python ingestion/load_data.py
```

---

### 5️⃣ Run dbt

```bash
cd dbt_project
dbt run
dbt test
```

---

### 6️⃣ Run Prefect

```bash
prefect deployment run main-flow
```

---

## 🧪 Data Quality

dbt tests include:

* not null
* unique
* relationships
* accepted values

---

## 📊 KPIs Example

* Number of patients
* Revenue per month
* Average visit duration
* Doctor performance
* Treatment success rate

---

## 🎯 Key Concepts Demonstrated

* Separation of storage & compute
* ELT approach
* Layered modeling
* Orchestrated pipelines
* BI dual consumption (Superset + Power BI)

---

## 🔮 Future Improvements

* Dockerization
* CI/CD with GitHub Actions
* Data lineage visualization
* Role-based access control
* Incremental models optimization

---

## 👨‍💻 Author

Ahmed Fadili
PhD in Life Sciences | Data & Analytics 


---



 
