# 📊 HPV Awareness Impact Analysis in Healthcare using Python + SQL + Streamlit
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)](https://streamlit.io/)

![alt text](documentation/Dashboard.gif)
- Dashboard Link : https://hpv-awareness-impact-analysis-david-singh.streamlit.app/

---

## 🚀 Executive Summary

* **Business Problem:** HPV remains a major public health challenge, with awareness gaps leading to low vaccination and preventive behaviors. Measuring the impact of awareness interventions is crucial.
* **Solution:** Conducted pre- and post-test surveys, built a structured database, analyzed awareness improvements, and deployed a **Streamlit dashboard** for interactive insights.
* **Key Results:**

  * Significant knowledge gains post-intervention (*Cohen’s d: large effect size*).
  * Reliable survey instrument (Cronbach’s α > 0.7).
  * Urban participants scored higher than rural counterparts.
* **Tools & Skills Used:** Python (Pandas, Plotly, Scikit-learn) | SQL (SQLite) | Streamlit | Statistical Testing (t-test, ANOVA, Wilcoxon) | Visualization | Data Engineering (ETL).

---

## 🏢 Project Background

* **Context:** HPV-related diseases (especially cervical cancer) are preventable, but awareness remains low. Public health programs often invest in interventions, yet evaluating their impact is challenging.
* **Business Relevance:** Insights help policymakers and NGOs optimize awareness campaigns by focusing resources where they have the most effect.
* **Artifacts:**

  * [📑 Blog Walkthrough](https://medium.com/@davidsingh.blogs/hpv-awareness-impact-analysis-end-to-end-data-analytics-project-2884fa7d6ea2)
  * [📊 Interactive Dashboard](https://hpv-awareness-impact-analysis-david-singh.streamlit.app/)

---

## 🗂️ Data Structure & Initial Checks

* **Sources:** Survey-based raw data in CSV/Excel (pre-test, post-test, demographics).
* **Schema:**

  * `demographic` (age, gender, education, residency) – 58 participants.
  * `pretest` (33 Qs + total score).
  * `post_test` (33 Qs + total score).
* **Processing Pipeline:**

  * `ingestion_db.py` → Ingest raw CSV/Excel → SQLite DB.
  * `hpv_db_utils.py` → Build structured demographic/pre/post tables → export summary Excel.
  * Cleaned dataset stored as `cleaned_hpv_data.csv`.

---

## 🔎 Methodology & Approach

1. **ETL & Data Cleaning** – automated ingestion, schema creation, normalization.
2. **EDA** – demographic breakdowns, score distributions, correlations.
3. **Statistical Analysis** –

   * Normality checks (Shapiro-Wilk).
   * Paired t-test & Wilcoxon Signed-Rank test for pre-post differences.
   * ANOVA for subgroup comparisons.
   * Effect size (Cohen’s d) & reliability (Cronbach’s α).
4. **Visualization & Dashboard** – interactive Streamlit app with Plotly.
5. **Business Translation** – actionable recommendations for healthcare interventions.

---

## 📊 Insights Deep Dive

### Category 1: Demographics

* Urban > Semi-Urban > Rural in awareness scores.
* Education level positively correlated with improvement (high school showed biggest jump).
* Balanced gender representation, with no significant score differences.

### Category 2: Knowledge Gains

* Pre-test vs Post-test → significant improvement (p < 0.001).
* Strongest effect for participants with low baseline scores.
* Cronbach’s α > 0.7 → reliable assessment tool.

### Category 3: Behavioral Targeting

* Rural participants had lower baseline and smaller improvements → need targeted reinforcement.
* Undergraduates and high school students showed the greatest relative knowledge gain.

---

## 📈 Results & Business Recommendations

* **Results:**

  * *Large, statistically significant* knowledge improvement.
  * Demographics less influential overall, but residency a key driver.
  * High validity and reliability of the survey tool.

* **Recommendations:**

  * Tailor campaigns for **rural communities** with additional reinforcement.
  * Deploy more resources at **high school and undergraduate levels**.
  * Use findings to optimize **resource allocation** in public health programs.

---

## ⚠️ Assumptions & Caveats

* Sample size = 58 participants (small for generalization).
* Residency labels assumed as categorical (Rural/Semi-Urban/Urban).
* Some missing demographic fields imputed with mode values.
* Pre/post scores capped at available question set (33 Qs).

---

## 🔮 Next Steps & Future Work

* Scale study to larger population samples across regions.
* Integrate vaccination uptake data to link awareness → behavior.
* Apply ML models for predicting high-risk demographics for awareness shortfall.
* Extend dashboard to policymakers with **real-time monitoring**.

---

## 🛠️ Tools & Skills Demonstrated

* **SQL:** Schema design, ingestion, table joins.
* **Python:** Pandas, NumPy, Plotly, Statsmodels, Scikit-learn.
* **Visualization:** Interactive Streamlit dashboard.
* **Data Engineering:** Automated ingestion + ETL with logging.
* **Statistics:** Paired t-test, ANOVA, Wilcoxon, Effect size, Cronbach’s α.

---

## 📂 Repository Structure

```
├── .gitignore
├── LICENSE
├── README.md
├── data
    ├── database
    │   └── HPV.db                                  # `SQLite` DB
    ├── processed_data                              
    │   ├── cleaned_hpv_data.csv                    # Final cleaned dataset
    │   ├── data_dictionary.csv                     # Data Dictionary 
    │   └── summary_data.xlsx                       # Cleaned data after `Excel` preprocessing
    └── raw_data
    │   └── raw_data.xlsx                           # Input survey files (CSV/Excel)
├── documentation
    ├── Dashboard.gif
    └── Final_Statistical_Report.docx
├── models
    ├── cleaned_hpv_data.pkl
    ├── data_dictionary.pkl
    ├── eda_figures.pkl
    └── stats_results.pkl
├── notebooks
    ├── 01_Data_Loading_and_Cleaning.ipynb
    ├── 02_Exploratory_Data_Analysis.ipynb
    ├── 03_Statistical_Analysis.ipynb
    └── 04_Reporting.ipynb
├── reports
    ├── figures
    │   ├── age_group_distribution.png
    │   ├── correlation_heatmap.png
    │   ├── education_distribution.png
    │   ├── gender_distribution.png
    │   ├── knowledge_score_distribution.png
    │   ├── residency_distribution.png
    │   ├── score_improvement_education.png
    │   ├── score_improvement_gender.png
    │   └── score_improvement_residency.png
    └── final
    │   └── HPV_Awareness_Impact_Report.docx
├── requirements.txt
└── scripts
    ├── app.py                                        # Streamlit Dashboard
    ├── hpv_db_utils.py                               # DB utilities & summary export
    └── ingestion_db.py                               # Raw data ingestion pipeline
```

---

## 📜 References & Sources

* Survey dataset (confidential, anonymized).
* WHO & CDC reports on HPV awareness and vaccination.
* Statistical methodology references: Shapiro-Wilk, Paired t-test, Cronbach’s α.