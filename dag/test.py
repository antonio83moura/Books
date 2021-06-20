# Antonio

import json
import pathlib
 
import airflow
import requests
import requests.exceptions as requests_exceptions
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
 

def my_func(p1, p2):
    return f"p1 -> {p1}, p2 -> {p2}"

dag = DAG(
   dag_id="my_dag",
   start_date=airflow.utils.dates.days_ago(14),
   schedule_interval="@daily",
   user_defined_macros={'report': my_func}

)



my_function = BashOperator(
   task_id="my_func",
   bash_command='echo "{{report(11, 44)}}"',
   dag=dag,
)
 
# download_launches >> get_pictures >> my_function >> notify

my_function

