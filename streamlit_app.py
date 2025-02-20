import streamlit as st
import sqlite3
import pandas as pd

st.title("My Streamlit App")

def get_data():
    conn = sqlite3.connect('data/database.db')
    # Example: Fetch data using pandas
    df = pd.read_sql_query("SELECT * FROM your_table", conn)
    conn.close()
    return df

df = get_data()
st.dataframe(df)  # Display the dataframe
# ... other Streamlit elements