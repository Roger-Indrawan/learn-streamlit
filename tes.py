import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
## **Palem Star Aluminium**

This is the **Palem Star Aluminium** We Sell Various of **Furniture** Here.

---
''')

# Upload CSV data
with st.sidebar.header('Palem Star Aluminium'):
    uploaded_file = st.sidebar.file_uploader("Tangga dan Jemuran", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
""")

# Pandas Profiling Report
if uploaded_file is not None:
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
