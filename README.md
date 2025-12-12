# Uber Pipeline Paris – Data Engineer Project (Jedha Lead)

## Overview
Pipeline end-to-end : Ingestion Uber/NYC Taxi data every 5 min → S3 raw → dbt transform → Airflow orchestrate → Streamlit dashboard.

## Structure
- 1-ingestion : Airbyte config
- 2-raw : S3 bucket check
- 3-transformed : dbt models
- 4-orchestration : Airflow DAG
- 5-dashboard : Streamlit app

## Setup
1. AWS S3 bucket: uber-raw-paris-2025
2. Airbyte Cloud: Import airbyte-connection.json
3. dbt Cloud: Connect to S3, run models
4. Astronomer: Deploy DAG
5. Streamlit: Deploy app.py

## Demo
[Live Dashboard](https://ton-app.streamlit.app)  
[Screenshots] (add images)

Built in 7 days for Jedha application – Dec 2025.