from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'data-engineer',
    'start_date': datetime(2025, 12, 1),
}

dag = DAG(
    'uber_pipeline_hourly',
    default_args=default_args,
    schedule_interval='@hourly',
    catchup=False
)

ingest = BashOperator(
    task_id='ingest_airbyte',
    bash_command='airbyte --config /path/to/airbyte-connection.json run',
    dag=dag
)

transform = BashOperator(
    task_id='dbt_run',
    bash_command='dbt run --models staging',
    dag=dag
)

ingest >> transform