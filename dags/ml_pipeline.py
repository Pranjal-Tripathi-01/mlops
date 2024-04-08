from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from data_load import load_data
from data_preprocess import data_preprocessing
from model_training import training_model
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 7),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1
}

git_repo_dir = 'https://github.com/Pranjal-Tripathi-01/mlops_assignment'


with DAG('ml_pipeline', default_args=default_args, 
    description='A simple DAG', 
    schedule_interval=None)as dag:

    task1 = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    task2 = PythonOperator(
        task_id='preprocess_data',
        python_callable=data_preprocessing
    )

    task3 = PythonOperator(
        task_id='train_model',
        python_callable=training_model
    )

    task4 = BashOperator(
        task_id='push_to_github',
        bash_command=f'cd {git_repo_dir} && git add . && git commit -m "$(git describe --tags --abbrev=0)-$(git rev-parse --short HEAD)" && git push origin master',
    )

    task1 >> task2 >> task3 >> task4
