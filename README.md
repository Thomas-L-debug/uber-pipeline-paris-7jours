# Uber Pipeline Paris – Data Engineer Project (Jedha Lead)

Pipeline end-to-end S3 → Streamlit live

## Structure
- 1-ingestion : config Airbyte (en backup)
- 2-raw : bucket S3 uber-raw-paris-2025 + check-bucket.py
- 5-dashboard : app.py Streamlit live

## Démo live
[https://uber-pipeline-paris-7jours.streamlit.app](https://uber-pipeline-paris-7jours-hd3qcmqxyyxgqnm9fotrapp.streamlit.app/)

## Technologies
- AWS S3
- Pandas + Plotly
- Streamlit Cloud (déploiement gratuit)

## Note sur les parties non activées

- **3-transformed** (dbt models) : Modèles prêts, mais non exécutés à cause des limitations du trial Snowflake sur les external stages S3 (création de stage avec credentials bloquée).
- **4-orchestration** (Airflow DAG) : DAG prêt, mais non déployé (Astronomer free tier limité pour ce POC).
- **Focus actuel** : Le pipeline fonctionnel est **S3 raw → Streamlit live** (lecture directe Parquet depuis S3, dashboard interactif).

Le projet montre la structure complète d’un pipeline, avec la partie live (S3 + dashboard) pleinement opérationnelle.

Prochaine étape en entreprise : déploiement dbt + Airflow sur un compte Snowflake payant ou Databricks.

Projet réalisé en 7 jours pour candidature Jedha Lead – Décembre 2025
