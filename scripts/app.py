import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

# Page configuration
st.set_page_config(page_title="HPV Awareness Dashboard", layout="wide")

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

# Score Distributions
st.header("Knowledge Score Improvement")
fig_scores = go.Figure()
fig_scores.add_trace(go.Histogram(x=filtered_df['pre_test_score'], name="Pre-Test Score", opacity=0.5, histnorm='density'))
fig_scores.add_trace(go.Histogram(x=filtered_df['post_test_score'], name="Post-Test Score", opacity=0.5, histnorm='density'))
fig_scores.update_layout(title="Pre- and Post-Test Score Distributions", xaxis_title="Knowledge Score", yaxis_title="Density", barmode="overlay")
st.plotly_chart(fig_scores, use_container_width=True)

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

# Interesting Fact
st.header("Interesting Fact")
st.write("The intervention was most effective for high school students, with some achieving score improvements up to 25 points, likely due to lower baseline knowledge compared to post-graduates, who showed minimal gains due to a ceiling effect.")

# Conclusion
st.header("Conclusion")
st.write("The intervention significantly improved HPV knowledge, particularly among undergraduates and high school students. Use the filters to explore specific demographic groups and their score improvements.")