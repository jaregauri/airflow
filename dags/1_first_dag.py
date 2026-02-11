from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator

@dag(
    dag_id="first_dag"
)
def first_dag():
    
    @task.python
    def first_task():
        print("this is the first task")

    @task.python
    def second_task():
        print("this is the second task")
    
    @task.python
    def third_task():
        print("this is the third task hkjhkj")

    @task.bash
    def bash_task_first():
        return "echo https://airflow.apache.org"
    
    bash_task_second = BashOperator(
        task_id = "bash_task_second",
        bash_command = "echo https://airflow.apache.org"
    )


    first = first_task()
    second = second_task()
    third = third_task()
    bash_first = bash_task_first()
    bash_second = bash_task_second

    first >> second >> third >> bash_first >> bash_second

first_dag()