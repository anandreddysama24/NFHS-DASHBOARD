import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title=NFHS Dashboard, layout=wide)

st.title(National Family Health Survey (NFHS) Dashboard)

# Load Data
@st.cache_data
def load_data()
    df = pd.read_csv(All India National Family Health Survey.csv)
    return df

df = load_data()

# Show Raw Data
if st.checkbox(Show Raw Data)
    st.dataframe(df)

st.sidebar.header(Filters)

# Select numeric columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

# Column selection
selected_column = st.sidebar.selectbox(Select Indicator, numeric_cols)

# State filter (if state column exists)
if State in df.columns
    selected_states = st.sidebar.multiselect(
        Select State(s),
        options=df[State].unique(),
        default=df[State].unique()
    )
    df = df[df[State].isin(selected_states)]

# Summary
st.subheader(📌 Summary Statistics)
st.write(df[selected_column].describe())

# Chart
st.subheader(📈 Visualization)

chart_type = st.radio(Select Chart Type, [Bar Chart, Line Chart, Histogram])

fig, ax = plt.subplots(figsize=(10, 5))

if chart_type == Bar Chart
    if State in df.columns
        sns.barplot(x=State, y=selected_column, data=df, ax=ax)
        plt.xticks(rotation=90)
    else
        sns.barplot(y=selected_column, data=df, ax=ax)

elif chart_type == Line Chart
    if State in df.columns
        sns.lineplot(x=State, y=selected_column, data=df, marker=o, ax=ax)
        plt.xticks(rotation=90)

elif chart_type == Histogram
    sns.histplot(df[selected_column], kde=True, ax=ax)

st.pyplot(fig)

st.markdown(---)
st.markdown(Dashboard created using Streamlit 🚀)
