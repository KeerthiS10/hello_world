from airflow.models import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    'owner': 'anuj',
    'depends_on_past': False,
    'start_date': datetime(2021, 4, 19),
    'retries': 0
}

dag = DAG(dag_id='DAG-3', default_args=default_args, catchup=False, schedule_interval='@once')

start = DummyOperator(task_id='start', dag=dag)
end = DummyOperator(task_id='end', dag=dag)

start >> end