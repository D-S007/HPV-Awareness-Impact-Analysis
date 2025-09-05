import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

# Page configuration
st.set_page_config(page_title="HPV Awareness Dashboard", layout="wide")

st.markdown(
    """
    🔗 [GitHub](https://github.com/d-s007/HPV-Awareness-Impact-Analysis) | 📝 [Blog](https://medium.com/@davidsingh.blogs/hpv-awareness-impact-analysis-end-to-end-data-analytics-project-2884fa7d6ea2)
    """,
    unsafe_allow_html=True
)

# Loading data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed_data/cleaned_hpv_data.csv")
    return df

# Initializing session state
if 'df' not in st.session_state:
    st.session_state.df = load_data()

df = st.session_state.df

# Sidebar for filters
st.sidebar.header("Filter Data")
age_filter = st.sidebar.multiselect("Age Group", options=df['Age_Label'].unique(), default=df['Age_Label'].unique())
gender_filter = st.sidebar.multiselect("Gender", options=df['Gender_Label'].unique(), default=df['Gender_Label'].unique())
education_filter = st.sidebar.multiselect("Education Level", options=df['Education_Label'].unique(), default=df['Education_Label'].unique())
residency_filter = st.sidebar.multiselect("Place of Residency", options=df['Place_of_Residency_Label'].unique(), default=df['Place_of_Residency_Label'].unique())

# Filter data
filtered_df = df[
    (df['Age_Label'].isin(age_filter)) &
    (df['Gender_Label'].isin(gender_filter)) &
    (df['Education_Label'].isin(education_filter)) &
    (df['Place_of_Residency_Label'].isin(residency_filter))
]

# Title
st.title("HPV Awareness Impact Analysis Dashboard")
st.divider()

# Demographic Distributions
st.header("Demographic Distributions")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Education Level")
    fig_edu = px.histogram(filtered_df, y="Education_Label", title="Education Level Distribution", 
                           category_orders={"Education_Label": ["High school", "Under graduation", "Post-graduation"]})
    st.plotly_chart(fig_edu, use_container_width=True)

    st.subheader("Age Group")
    fig_age = px.histogram(filtered_df, y="Age_Label", title="Age Group Distribution",
                           category_orders={"Age_Label": ["15-19 Years", "19-24 Years", "24 Years and above"]})
    st.plotly_chart(fig_age, use_container_width=True)

with col2:
    st.subheader("Place of Residency")
    fig_res = px.histogram(filtered_df, y="Place_of_Residency_Label", title="Place of Residency Distribution",
                           category_orders={"Place_of_Residency_Label": ["Rural", "Semi-Urban", "Urban"]})
    st.plotly_chart(fig_res, use_container_width=True)

    st.subheader("Gender Distribution")
    gender_counts = filtered_df['Gender_Label'].value_counts()
    fig_gender = px.pie(values=gender_counts.values, names=gender_counts.index, title="Gender Distribution")
    st.plotly_chart(fig_gender, use_container_width=True)

st.divider()

# Score Distributions
st.header("Knowledge Score Improvement")
fig_scores = go.Figure()
fig_scores.add_trace(go.Histogram(x=filtered_df['pre_test_score'], name="Pre-Test Score", opacity=0.5, histnorm='density'))
fig_scores.add_trace(go.Histogram(x=filtered_df['post_test_score'], name="Post-Test Score", opacity=0.5, histnorm='density'))
fig_scores.update_layout(title="Pre- and Post-Test Score Distributions", xaxis_title="Knowledge Score", yaxis_title="Density", barmode="overlay")
st.plotly_chart(fig_scores, use_container_width=True)

st.divider()

# Score Improvement by Demographics
st.header("Score Improvement by Demographics")
col3, col4 = st.columns(2)

with col3:
    st.subheader("By Education Level")
    fig_box_edu = px.box(filtered_df, x="score_improvement", y="Education_Label", title="Score Improvement by Education Level",
                         labels={"score_improvement": "Score Improvement (Post - Pre)", "Education_Label": "Education Level"})
    st.plotly_chart(fig_box_edu, use_container_width=True)

with col4:
    st.subheader("By Gender")
    fig_box_gender = px.box(filtered_df, x="score_improvement", y="Gender_Label", title="Score Improvement by Gender",
                            labels={"score_improvement": "Score Improvement (Post - Pre)", "Gender_Label": "Gender"})
    st.plotly_chart(fig_box_gender, use_container_width=True)

st.divider()

# -- Correlation Heatmap --
st.header("Correlation Heatmap")
corr_matrix = filtered_df.corr(numeric_only=True)
fig_corr = px.imshow(corr_matrix, text_auto=True, color_continuous_scale="RdBu_r",
                     aspect="auto", title="Correlation Heatmap")
st.plotly_chart(fig_corr, use_container_width=True)

st.divider()

# -- Statistical Analysis Results --
import pickle

with open("models/stats_results.pkl", "rb") as f:
    stats_results = pickle.load(f)

st.header("Statistical Analysis Results")

# Show summary table
st.subheader("Overall Test Results")
st.dataframe(stats_results["summary_table"])

# Normality Tests
st.subheader("Normality Checks")
st.write(f"Pre-Test: W={stats_results['normality']['pre']['stat']:.3f}, "
         f"p={stats_results['normality']['pre']['p']:.3f}")
st.write(f"Post-Test: W={stats_results['normality']['post']['stat']:.3f}, "
         f"p={stats_results['normality']['post']['p']:.3f}")

# Paired Tests
st.subheader("Pre vs Post Tests")
st.write(f"Paired t-test: t={stats_results['paired_tests']['t_test']['t']:.3f}, "
         f"p={stats_results['paired_tests']['t_test']['p']:.3f}")
st.write(f"Wilcoxon Signed-Rank: W={stats_results['paired_tests']['wilcoxon']['W']:.3f}, "
         f"p={stats_results['paired_tests']['wilcoxon']['p']:.3f}")
st.write(f"Cohen's d: {stats_results['paired_tests']['cohens_d']:.2f}")
st.write(f"Statistical Power: {stats_results['paired_tests']['power']:.3f}")

# ANOVA
st.subheader("ANOVA by Education")
anova = stats_results['anova']['education']
st.write(f"F={anova['F']:.3f}, p={anova['p']:.3f}, Bonferroni-corrected p={anova['p_corr']:.3f}")

# Reliability
st.subheader("Reliability (Cronbach's Alpha)")
st.write(f"Pre-Test: {stats_results['cronbach']['alpha_pre']:.3f}")
st.write(f"Post-Test: {stats_results['cronbach']['alpha_post']:.3f}")

# -- Data Dictionary --
with open("models/data_dictionary.pkl", "rb") as f:
    data_dict = pickle.load(f)

st.header("Data Dictionary")
st.table(pd.DataFrame(list(data_dict.items()), columns=["Variable", "Description"]))
st.divider()

# -- Key Insights & Actionable Conclusions --
st.header("Key Insights & Actionable Conclusions")
st.markdown("""
- **Awareness improved significantly** after the intervention (large effect size).
- **Reliability** of the survey tool is acceptable (Cronbach’s α > 0.7).
- **Score improvements strongest** among low baseline groups (e.g., high school students).
- **Demographics had minimal influence**, except residency: urban > semi-urban > rural.
- **Action:** Tailor more support for rural participants, reinforce higher scorers to prevent plateau.
""")

# Conclusion
st.header("Conclusion")
st.write("The intervention significantly improved HPV knowledge, particularly among undergraduates and high school students. Use the filters to explore specific demographic groups and their score improvements.")
