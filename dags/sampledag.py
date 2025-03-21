from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def triggered_task(**kwargs):
    print("Hello from Azure Data Factory!")
    print("DAG run config:", kwargs.get('dag_run').conf)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
}

with DAG(
    dag_id='trigger_from_adf_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,  # So it can be triggered manually
    catchup=False
) as dag:

    task = PythonOperator(
        task_id='print_hello',
        python_callable=triggered_task,
        provide_context=True
    )
