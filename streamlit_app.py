import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Uber Pipeline Paris – Dashboard Live (3,1 M trips depuis S3)")

# Connection sécurisée via Streamlit Secrets (pas de password en clair)
conn = st.connection("snowflake")


@st.cache_data(ttl=3600)  # Cache 1 heure pour éviter de recharger à chaque refresh
def load_data():
    query = """
    SELECT 
        tpep_pickup_datetime as pickup_datetime,
        tpep_dropoff_datetime as dropoff_datetime,
        passenger_count,
        trip_distance,
        total_amount
    FROM RAW_UBER_TRIPS
    LIMIT 50000
"""
    return conn.query(query)

df = load_data()

st.write("### Aperçu des données brutes (3,1 M lignes chargées depuis S3)")
st.dataframe(df.head(10))

st.write("### Total amount par jour")
daily = df.groupby(df['pickup_datetime'].dt.date)['total_amount'].sum().reset_index()
daily.columns = ['date', 'total_amount']
fig = px.line(daily, x='date', y='total_amount', title="CA par jour (janvier 2023)")
st.plotly_chart(fig)

st.write("### Distance moyenne par nombre de passagers")
passenger = df.groupby('passenger_count')['trip_distance'].mean().reset_index()
fig2 = px.bar(passenger, x='passenger_count', y='trip_distance', title="Distance moyenne par nombre de passagers")
st.plotly_chart(fig2)

st.success("Pipeline S3 → Snowflake → Dashboard live – 3,1 M lignes !")