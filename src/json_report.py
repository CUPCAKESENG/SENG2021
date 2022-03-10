import json
import os
from datetime import datetime
from jwt import encode
from config import SALT, SECRET

"""
Report structure:
    {
        'file_size': 0,
        'file_name': '',
        'file_type': '',
        'sender': '',
        'received_time': 0,
        'created_time': 0,
        'dump_time': 0,
        'errors': []
    }
"""

def create_json_report(report):
    if not os.path.exists("./communication_report"):
        os.makedirs("./communication_report")

    if not all (key in report for key in ("sender", "received_time", "dump_time")):
        return False

    payload = {
        'sender': report["sender"],
        'time': str(report["received_time"])
    }
    token = encode(payload, SECRET)

    DATA_STORE_PATH = "./communication_report/" + token[-10:] + ".json"

    with open(DATA_STORE_PATH, "w") as FILE:
        report["dump_time"] = datetime.now()
        json.dump(report, FILE, default=str)
        FILE.close()

    return DATA_STORE_PATH