from ast import Raise
import os

initial_report = {
    'file_size': 0,
    'file_name': '',
    'file_type': '',
    'sender': '',
    'receieved_time': 0,
    'created_time': 0,
    'errors': {}
}

class Datastore:
    def __init__(self):
        self.__store = initial_report
    
    def get(self):
        return self.__store

    def set(self, store):
        self.__store = store

global data_store

data_store = Datastore()

DATA_STORE_PATH = "./communication_report/report.json"

if not os.path.exists("./communication_report"):
    os.makedirs("./communication_report")
