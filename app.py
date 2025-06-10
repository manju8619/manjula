import streamlit as st
import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('bus_data.db')
cursor = conn.cursor()

# Title
st.title("🚌 Redbus Bus Data Explorer")

# Load data
df = pd.read_sql_query("SELECT * FROM bus_routes", conn)

# Filters
with st.sidebar:
    st.header("🔍 Filter Options")
    bustypes = df['bustype'].dropna().unique()
    selected_type = st.selectbox("Select Bus Type", options=["All"] + list(bustypes))

    routes = df['route_name'].dropna().unique()
    selected_route = st.selectbox("Select Route Name", options=["All"] + list(routes))

# Apply filters
if selected_type != "All":
    df = df[df['bustype'] == selected_type]

if selected_route != "All":
    df = df[df['route_name'] == selected_route]

# Show Data
st.dataframe(df)

# Summary
st.write(f"Total Results: {len(df)}")

conn.close()
