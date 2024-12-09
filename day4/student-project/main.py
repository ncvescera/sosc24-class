import mlflow
import click
import os
import sys



#@click.command()
#@click.option("--data-url", default="tt", type=str)
def workflow():
    # download_data_run = mlflow.run(".", "download_data", parameters={"data_url": data_url}, env_manager="local") 
    # download_data_run.wait()
    # artifact_path = mlflow.get_run(download_data_run.run_id).info.artifact_uri
    #prepare_train_test_run = mlflow.run(".", "prepare_train_test", parameters={"data_url": data_url}, env_manager="local") 
    #prepare_train_test_run.wait()
    #artifact_path = mlflow.(prepare_train_test_run.run_id).info.artifact_uri
    
    train_run = mlflow.run(".", "train", parameters={"learning_rate": 1e-4, "batch_size": 32, "n_epochs": 1}, env_manager="local") 
    train_run.wait()
    
    artifact_path = mlflow.get_run(train_run.run_id).info.artifact_uri

    eval_run = mlflow.run(".", "eval", parameters={"model": artifact_path}, env_manager="local") 
    eval_run.wait()
if __name__ == "__main__":
    workflow()