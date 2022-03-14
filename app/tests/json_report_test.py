"""
SENG2021 - Group Cupcake
File: json_report_test.py
    Description: Static tests for json_report.py code
"""

from ast import For
import sys
import os
import json
from app.src.error import FormatError
import pytest
from datetime import datetime
# from app.src.data_store import data

from app.src.auth import register, is_valid
from app.src.data_store import clear
from app.src.json_report import create_json_report
# not sure how to properly Import  -> this is a temporary solution
sys.path.insert(0, '..')


@pytest.fixture
def setup():
    clear()
    token = register("owner@streams.com.au", "i am the owner",
                     "Jerry", "Thompson")["token"]
    time = datetime.now()
    report = {
        'file_size': 100,
        'file_name': 'Report A',
        'sender': 'Owner',
        'received_time': str(time),
        'created_time': str(time),
        'dump_time': 0,
    }
    bad_report = {
        'file_size': 150,
        'file_name': 'Report B',
        'sender': 'Owner',
        'created_time': str(time),
        'dump_time': 0,
    }

    return {
        "token": token,
        "time": time,
        "report": report,
        "bad_report": bad_report
    }


def test_json_report(setup):
    """
    Valid JSON Report Tests
        Checks if the json_create_report function works
    """
    path = create_json_report(setup["report"])
    with open(path, "r", encoding="ascii") as file:
        json_object = json.load(file)
        assert json_object == setup["report"]

def test_json_report_format_error(setup):
    """
    Error JSON Report Tests
        Checks if the json_create_report returns FormatError
    """
    with pytest.raises(FormatError):
        create_json_report(setup["bad_report"])