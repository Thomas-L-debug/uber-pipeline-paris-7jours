import streamlit as st
import pandas as pd
import boto3
import io
import plotly.express as px

st.set_page_config(page_title="Uber Pipeline Paris – Live Dashboard", layout="wide")

st.title("🚕 Uber Pipeline Paris – Dashboard Live depuis S3")

st.markdown("""
Pipeline Data Engineer complet :
- Bucket S3 `uber-raw-paris-2025`
- Fichier Parquet Uber/NYC Taxi (2M lignes)
- Lecture directe depuis S3 (sans warehouse)
- Dashboard interactif
""")

# Config AWS (à mettre en secrets sur Streamlit Cloud)
s3 = boto3.client('s3',
                  aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
                  aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
                  region_name="eu-west-3")

bucket = "uber-raw-paris-2025"
key = "Raw/uber_trips/yellow_tripdata_2023-01.parquet"  # chemin exact

# Lecture du Parquet depuis S3
with st.spinner("Chargement des 2 millions de lignes depuis S3..."):
    obj = s3.get_object(Bucket=bucket, Key=key)
    df = pd.read_parquet(io.BytesIO(obj['Body'].read()))

st.success(f"{len(df):,} lignes chargées en live depuis S3 !")

st.subheader("10 premières lignes")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("Répartition des montants totaux (total_amount)")
fig_bar = px.histogram(df, x="total_amount", nbins=50, title="Distribution des total_amount")
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("Distance moyenne par nombre de passagers")
fig_line = px.bar(df.groupby('passenger_count')['trip_distance'].mean().reset_index(), 
                  x='passenger_count', y='trip_distance', title="Trip distance moyenne par passenger_count")
st.plotly_chart(fig_line, use_container_width=True)

st.caption("Projet Data Engineer pour Jedha Lead – Décembre 2025 | Repo GitHub : https://github.com/Thomas-L-debug/uber-pipeline-paris-7jours")