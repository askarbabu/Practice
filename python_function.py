# def hi(input):
#     print('hi {}'.format(input))
#
# def hey(input):
#         print('hey {}'.format(input))


import os
from random import random, randint
from mlflow import log_metric, log_param, log_artifacts
import mlflow

with mlflow.start_run(experiment_id=0):
    # Log a parameter (key-value pair)
    log_param("param1", randint(0, 100))

    # Log a metric; metrics can be updated throughout the run
    log_metric("foo", random())

    # Log an artifact (output file)
    if not os.path.exists("outputs_mlf"):
        os.makedirs("outputs_mlf")
    with open("outputs_mlf/test.txt", "w") as f:
        f.write("hello world!")

    log_artifacts("outputs_mlf")
