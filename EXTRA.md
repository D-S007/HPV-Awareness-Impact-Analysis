# 1 To run ingestion_db.py script : 
Inside terminal `python scripts/ingestion_db.py`

# If sqlalchemy error in ipynb file, 
1. activate venv
2. Run `/home/Davcote/Desktop/HPV-Awareness-Impact-Analysis/venv/bin/python -m pip install sqlalchemy`

`print("df_demo_full columns before renaming:", df_demo_full.columns.tolist())`
To check datatype of columns before mapping
demographic_cols_map = {
    '1': 'Age', 
    '2': 'Gender', 
    '3': 'Place_of_Residency', 
    '4': 'Education',
    '5': 'Vaccination_Status', 
    '6': 'Health_Care_Access', 
    '7': 'Occupation_of_Parents',
    '8': 'Family_Income_per_Month'
}

# Add "nbkviewer" with each notebook so it loads correctly

## 📊 Power BI Dashboard Plan
Finally, to create a compelling visual summary:

Connect to Data: Open Power BI Desktop. Click Get Data -> Text/CSV and select your cleaned_hpv_data.csv file from the data/processed/ folder.

Create Page 1: "Demographic Overview"

Cards: Use Card visuals to show "Total Participants" (Count of Sno), "Average Age", and "Average Pre-Test Score".

Charts: Use Donut charts for Gender_Label and Pie charts for Place_of_Residency_Label. Use a horizontal Bar chart for Education_Label.

Create Page 2: "Intervention Impact"

KPIs: Use two Gauge visuals to show the "Average Pre-Test Score" and "Average Post-Test Score" side-by-side to highlight the increase.

Distribution: Use a Line chart to plot both pre_test_score and post_test_score to show the shift.

Impact by Group: Use a Clustered Bar Chart to show the "Average score_improvement" by Education_Label to see which group benefited most.

Create Page 3: "Predictive Insights"

Feature Importance: Import the image of the feature importance plot you saved from Notebook 4.

Key Drivers: Use Text Boxes to summarize the findings. For example: "The predictive model identified Education and Family Income as the strongest drivers of knowledge gain. Future interventions should focus on tailoring content for different educational backgrounds."