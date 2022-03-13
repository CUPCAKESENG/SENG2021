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
    if not os.path.exists("../communication_report"):
        os.makedirs("../communication_report")

    if not all (key in report for key in ("sender", "received_time")):
        raise FormatError(description="Communication report is not in the right format.")

    payload = {
        "sender": report["sender"],
        "time": report["received_time"]
    }
    token = encode(payload, SECRET)

    report_path = "../communication_report/" + token[-10:] + ".json"

    with open(report_path, "w", encoding="ascii") as file:
        report["dump_time"] = datetime.now()
        json.dump(report, file, default=str)
        file.close()

    return report_path