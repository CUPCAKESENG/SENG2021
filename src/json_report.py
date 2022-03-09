import json
import os
from datetime import datetime

"""
Report structure:
    {
        'id': 0,
        'file_size': 0,
        'file_name': '',
        'file_type': '',
        'sender': '',
        'receieved_time': 0,
        'created_time': 0,
        'dump_time': 0,
        'errors': []
    }
"""

def create_json_report(report):
    if not os.path.exists("./communication_report"):
        os.makedirs("./communication_report")

    DATA_STORE_PATH = "./communication_report/" + str(report["id"]) + ".json"

    for file in os.listdir("./communication_report"):
        if file == (str(report["id"]) + ".json"):
            return False

    with open(DATA_STORE_PATH, "w") as FILE:
        report["dump_time"] = datetime.now()
        json.dump(report, FILE, default=str)
        FILE.close()

    return DATA_STORE_PATH