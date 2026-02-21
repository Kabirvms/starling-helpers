import os
import yaml
import logging

logging.basicConfig(filename=config("LOG_FILE"), encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)


def env(variable_name: str) -> str:
    variable = os.environ.get(variable_name)
    if variable is None:
        logger.error("Please run setup.py or add the env for %s", variable_name)
        raise EnvironmentError(f"Missing required environment variable: {variable_name}")
    return variable
        
def config(variable_name: str) -> str:
    data = yaml.safe_load(open("config.yml"))
    if not isinstance(data, dict):
        raise ValueError(f"config.yml is malformed — expected a dict, got {type(data).__name__}: {data!r}")
    variable = data.get(variable_name)
    if variable is None:
        logger.error("Please run setup.py or add the config for %s", variable_name)
        raise KeyError(f"Missing required config key: {variable_name}")
    return variable