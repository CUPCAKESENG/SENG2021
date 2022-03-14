"""
SENG2021 - Group Cupcake
File: json_report.py
    Description: Creates a JSON communication report
"""

import json
import os
from datetime import datetime
from jwt import encode
from app.src.error import FormatError
from app.src.config import SECRET

def create_json_report(report):
    """
    Creates JSON communication report.
        Params: report
        Returns: report_path
        Errors: FormatError
    """
    if not os.path.exists("app/communication_report"):
        os.makedirs("app/communication_report")

    if not all (key in report for key in ("sender", "received_time", "filename", "path")):
        raise FormatError("Communication report is not in the right format.")

    payload = {
        "sender": report["sender"],
        "time": report["received_time"],
        "file_size": os.path.getsize(report["path"]),
        "file_name": report["filename"]
    }

    token = encode(payload, SECRET)
    payload["token"] = token[-10:]

    report_path = "app/communication_report/" + token[-10:] + ".json"

    print(report_path)

    with open(report_path, "w", encoding="ascii") as file:
        report["dump_time"] = datetime.now()
        json.dump(report, file, default=str)

    return payload