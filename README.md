# HPV Awareness Campaign: Impact Analysis and Predictive Modeling

## 🎯 Project Objective
This project analyzes the effectiveness of an educational intervention aimed at increasing awareness about HPV among youth. The analysis moves from initial data cleaning and statistical testing to building a predictive model that identifies the demographic factors most crucial for successful knowledge uptake. The final results are presented in an interactive Power BI dashboard.

---
## ❓ Key Questions
1.  What was the demographic makeup of the study participants?
2.  Was there a statistically significant increase in HPV knowledge after the intervention?
3.  Which demographic groups showed the most significant improvement?
4.  Can we predict a participant's post-intervention knowledge score based on their demographic profile?
5.  What are the most important factors influencing knowledge improvement?

---
## ⚙️ Tech Stack & Workflow
This project utilizes a modern data stack to showcase skills from data ingestion to final reporting.


1.  **Data Ingestion & Storage:** Raw CSV data is cleaned and structured using **Pandas**, then loaded into a **SQLite** database.
2.  **Analysis & Modeling:** Data is queried from SQLite into Jupyter Notebooks. **Pandas** and **NumPy** are used for manipulation, **Matplotlib/Seaborn** for initial visualization, **SciPy** for statistical testing, and **Scikit-learn** for machine learning.
3.  **Reporting & Visualization:** Key analytical findings and predictions are visualized in an interactive **Power BI** dashboard connected to the SQLite database.

---
## 🚀 Key Findings
* The educational intervention led to a statistically significant increase in mean knowledge scores from X to Y (p < 0.001).
* The feature importance analysis from our Random Forest model revealed that **Education Level** and **Place of Residency** are the strongest predictors of post-intervention knowledge.
* [Add a compelling screenshot of your Power BI dashboard here]

---
## 🛠️ How to Run This Project
1. Clone the repository:
   ```bash
   git clone [https://github.com/d-s007/HPV-Awareness-Impact-Analysis.git](https://github.com/d-s007/HPV-Awareness-Impact-Analysis.git)
   ```
2. Navigate to the project directory:
   ```bash
   cd HPV-Awareness-Impact-Analysis
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Jupyter Notebooks in the following order:
   - `01_Data_Ingestion_and_DB_Setup.ipynb`
   - `02_EDA_and_Statistical_Analysis.ipynb`
   - `03_Predictive_Modeling.ipynb`
