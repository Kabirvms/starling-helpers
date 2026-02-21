import os
import uuid
import time
import logging
import yaml
import requests
from requests.adapters import HTTPAdapter
from dotenv import load_dotenv

load_dotenv()


config = load_config()
LOG_FILE = config["LOG_FILE"]
SLEEP_TIME = config["SLEEP_TIME"]
logging.basicConfig(filename=config(LOG_FILE), encoding="utf-8", level=logging.DEBUG)
logger = logging.getLogger(__name__)

