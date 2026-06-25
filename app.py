import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data Explorer")

uploaded_file = st.file_uploader("apple_stock", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Preview")
    st.dataframe(df.head())
    
    st.subheader("Columns found")
    st.write(list(df.columns))
    
    # let user pick date column
    date_col = st.selectbox("Select the date column", df.columns)
    
    # let user pick variable to plot
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    variable = st.selectbox("Select variable to plot", numeric_cols)
    
    # plot
    fig = px.line(df, x=date_col, y=variable, title=f"{variable} over time")
    st.plotly_chart(fig)
