import os
import uuid
import time
import logging
import yaml
import requests
from requests.adapters import HTTPAdapter
from dotenv import load_dotenv

load_dotenv()


def load_config(path: str = "config.yml") -> dict:
    with open(path, "r") as f:
        return yaml.safe_load(f)

config = load_config()
LOG_FILE = config["LOG_FILE"]
SLEEP_TIME = config["SLEEP_TIME"]
logging.basicConfig(filename=LOG_FILE, encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)