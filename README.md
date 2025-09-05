# HPV Awareness Campaign: Statistical Impact Analysis 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)](https://streamlit.io/)

![alt text](documentation/Dashboard.gif)
- Dashboard Link : https://hpv-awareness-impact-analysis-david-singh.streamlit.app/

## Project Overview
This repository contains an end-to-end data analysis pipeline for evaluating the impact of an HPV awareness intervention among youth in District Sitapur, India. It includes data ingestion, cleaning, EDA, statistical analysis, automated reporting, and an interactive Streamlit dashboard.

### Key Features
- **Data Pipeline**: Ingest raw CSV/Excel into SQLite, clean and merge datasets.
- **EDA**: Interactive Plotly visualizations for demographics and scores.
- **Stats**: Tests like paired t-test, Wilcoxon, ANOVA, Cronbach's Alpha.
- **Reporting**: Automated DOCX report generation.
- **Dashboard**: Streamlit app for filtering and exploring results.

### Directory Structure
- `data/`: Raw and processed data (e.g., `cleaned_hpv_data.csv`).
- `models/`: Pickled artifacts (e.g., stats results, figures).
- `notebooks/`: Jupyter notebooks for each stage (01-04).
- `scripts/`: Utility scripts (e.g., `hpv_db_utils.py`, `ingestion_db.py`).
- `reports/`: Generated DOCX and figures.
- `logs/`: Log files for debugging.
- `app.py`: Streamlit dashboard script.

## Installation
1. Clone the repo:
   ```
   git clone https://github.com/d-s007/HPV-Awareness-Impact-Analysis.git
   cd HPV-Awareness-Impact-Analysis
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   (Assumed requirements: pandas, numpy, sqlite3, plotly, streamlit, python-docx, scipy, pingouin, statsmodels)

## Usage
### Run Notebooks
- Start with `01_Data_Loading_and_Cleaning.ipynb` to process data.
- Proceed to EDA, Stats, and Reporting notebooks.

### Database Setup
- Run `ingestion_db.py` to ingest raw data into `data/database/HPV.db`.

### Dashboard
- Launch the Streamlit app:
  ```
  streamlit run scripts/app.py
  ```
- Access at `http://localhost:8501`. Use sidebar filters to explore.

### Generate Report
- Run `04_Reporting.ipynb` to create `reports/final/HPV_Awareness_Impact_Report.docx`.

## Data Sources
- Raw data: Demographics, pre/post-test scores (33 questions each).
- Processed: Merged CSV with labels and improvement scores.

## Key Results
- Significant knowledge improvement (p<0.001, large effect size).
- Insights: Tailor support for rural and low-education groups.


## License
MIT License. See [LICENSE](LICENSE) for details.

## Acknowledgments
- Inspired by public health data needs.
- Tools: Python ecosystem, Streamlit.
