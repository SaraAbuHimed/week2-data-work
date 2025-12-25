# Week 2 Data Pipeline — ETL + EDA

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline and exploratory data analysis (EDA) for order and user data.

---

## Setup (using `uv`)

### 1. Install `uv` (if not already installed)
```bash
pip install uv
```
### 2. Create a virtual environment
```bash
uv venv
```

### 3. Activate the virtual environment
```bash
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate    # Windows
```

## 4. Install dependencies
```bash
uv pip install -r requirements.txt
```


## How to run the ETL

From the project root directory, run:
```bash
python scripts/run_etl.py
```

This will:
- Load raw CSV files from data/raw/
- Clean and transform the data
- Join orders with users
- Generate analytics features and flags
- Write processed outputs and run metadata


## Where outputs go

```bash
data/processed/
├── orders_clean.parquet
├── users.parquet
├── analytics_table.parquet
└── _run_meta.json
```
- **orders_clean.parquet:** Orders-only table with cleaned fields
- **users.parquet:** Cleaned users table
- **analytics_table.parquet:** Final analytics table (one row per order)
- **_run_meta.json:** Metadata about the ETL run (row counts, missingness, join coverage, config paths)


## How to run the EDA notebook

### 1. Start Jupyter:
```bash
jupyter notebook
```

### 2. Open:
```bash
notebooks/eda.ipynb
```

### 3. Run all cells to reproduce the exploratory analysis using the processed data in data/processed/.


## Notes
- The ETL pipeline is idempotent and can be safely re-run.
- Time-based features are derived from UTC timestamps.
- Outliers in order amounts are winsorized, with flags preserved for analysis.

