#!/bin/bash

export MLFLOW_TRACKING_INSECURE_TLS=true
export MLFLOW_TRACKING_URI=http://localhost:5000/

# mlflow experiments create -n FinalTest
mlflow run ./ --env-manager=local --experiment-name FinalTest --run-name Main