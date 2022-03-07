import json
import time
from data_store import data_store

DATA_STORE_PATH = "./communication_report/report.json"

with open(DATA_STORE_PATH, "w") as FILE:
    store = data_store.get()
    json.dump(store, FILE)
    FILE.close()