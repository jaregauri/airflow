from airflow.sdk import dag, task

@dag(
    dag_id="xcom_dag"
)
def xcom_dag():
    
    @task.python
    def first_task():
        orignal_data = {"data" : [1, 2, 3]}
        return orignal_data

    @task.python
    def second_task(data:dict):
        first_task_data = data["data"]
        transformed_data = first_task_data*2
        transformed_data_dict = {"transformed_data" : transformed_data}
        return transformed_data_dict
    
    @task.python
    def third_task(data:dict):
        second_task_data = data["transformed_data"]
        transformed_data_v2 = second_task_data*0
        transformed_data_dict_v2 = {"transformed_data_v2" : transformed_data_v2}
        return transformed_data_dict_v2


    first = first_task()
    second = second_task(first)
    third = third_task(second)
   

    first >> second >> third 

xcom_dag()