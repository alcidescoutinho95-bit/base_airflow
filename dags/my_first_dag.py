from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_airflow():
    print("✅ Airflow está funcionando corretamente!")

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False,
}

with DAG(
    dag_id='dag_teste_simples_V2',
    description='Uma DAG simples para teste do ambiente',
    default_args=default_args,
    schedule_interval='@once',  # roda uma vez
    tags=['teste'],
) as dag:

    tarefa_hello = PythonOperator(
        task_id='diga_ola',
        python_callable=hello_airflow,
    )

    # tarefa_hello