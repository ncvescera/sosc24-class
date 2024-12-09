#!/bin/bash

papermill 2-Project-Day3.ipynb output.ipynb -p learning_rate 0.001 -p batch_size 100 -p n_epochs 30