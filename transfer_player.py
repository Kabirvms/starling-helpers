from tools import load_config_directory
from datetime import datetime


directories_of_config = load_config_directory()
auto_transfer_items = directories_of_config["auto_transfer"]

for item in auto_transfer_items:
