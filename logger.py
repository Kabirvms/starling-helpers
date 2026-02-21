from datetime import datetime
from tools import config

class Logger:
    def __init__(self):
        self.filetitle = config("LOG_FILE")
        self.mode = config("LOG_MODE")
        self.filename = self.filetitle + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
        
    def save(self, message: str):
        with open(self.filename, self.mode) as file:
            file.write(message)

    def info(self, message: str):
        self.save(message)
        print(message)
        
    def error(self, message: str):
        self.save(message)
        print(message)
        
    def critical(self, message: str):
        self.save(message)
        print(message)
        raise Exception(message)