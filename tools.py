import os


def env(variable_name):
    variable = os.environ.get(variable_name)
    if variable == "None":
        logger.error(f"Please run setup.py or add the env for {variable_name}")