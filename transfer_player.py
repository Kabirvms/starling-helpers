from tools import load_config_directory,env
from datetime import datetime

PRIMARY_ACCOUNT = env("PRIMARY_ACCOUNT")
directories_of_config = load_config_directory()
auto_transfer_items = directories_of_config["auto_transfer"]

for item in auto_transfer_items:
    if auto_transfer_items["item"]["frequency"] == "weekly":
        if auto_transfer_items["item"]["day"] == datetime.now().strftime("%A").lower():
            if 
            
