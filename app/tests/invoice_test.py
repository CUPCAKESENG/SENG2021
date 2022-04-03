"""
SENG2021 - Group Cupcake
File: invoice_test.py
    Description: Static tests for invoice_test.py code
"""

from ast import For
from doctest import REPORT_CDIFF
import sys
import os
import pytest
import json
import requests
import time
# from app.src.data_store import data

from app.src.error import PayloadError, FormatError, AccessError
from app.src.invoice import receive, update
from app.tests.request_wrappers import register_v1, delete_v1, list_v1, clear_v1
# not sure how to properly Import  -> this is a temporary solution
sys.path.insert(0, '..')

def process_status_code(response):
    if response.status_code == 406:
        raise PayloadError(description=response.reason)
    elif response.status_code == 417:
        raise FormatError(description=response.reason)
    elif response.status_code == 403:
        raise AccessError(description=response.reason)

    return response.json()

@pytest.fixture
def setup():
    clear_v1()
    token = register_v1("owner@streams.com.au", "i am the owner",
                     "Jerry", "Thompson")["token"]
    invoice = open("app/tests/files/sample.xml", "r")
    wrong_format = open("app/tests/files/a.txt", "r")
    updated_invoice = open("app/tests/files/updated_invoice.xml", "r")
    wrong_format_2 = open("app/tests/files/b.txt", "r")
    receive_url = "http://localhost:5000/invoice/receive"
    update_url = "http://localhost:5000/invoice/update"

    return {
        "token": token,
        "invoice": invoice,
        "wrong_format": wrong_format,
        "wrong_format_2": wrong_format_2,
        "updated_invoice": updated_invoice,
        "receive_url": receive_url,
        "update_url": update_url
    }


def test_receive(setup):
    """
    Valid Receive Tests
        Checks if the receive function works
    """
    assert list_v1(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "0"})

    invoice = list_v1(setup["token"])[0]

    assert invoice["path"] == "app/invoices_received\\jerrythompson_0.xml"
    assert invoice["id"] == 0
    assert invoice["filename"] == "jerrythompson_0.xml"
    assert invoice["output_format"] == 0
    assert invoice["deleted"] == False
    assert invoice["sender"] == "Jerry Thompson"
    

def test_format_error_receive(setup):
    """
    Error Receive Tests
        Checks if receive raises FormatError
    """

    with pytest.raises(FormatError):
        response = requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "4"})
        process_status_code(response)

    with pytest.raises(FormatError):
        response = requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "a"})
        process_status_code(response)

    with pytest.raises(FormatError):
        response = requests.post(setup["receive_url"], files={
                      "invoice": setup["invoice"]}, data={"token":"bad token", "output_format": "0"})
        process_status_code(response)

def test_update(setup):
    """
    Valid Update Tests
        Checks if the update function works
    """
    assert list_v1(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "0"})
    invoice = list_v1(setup["token"])[0]
    assert invoice["path"] == "app/invoices_received\\jerrythompson_0.xml"
    original_time = os.path.getmtime(invoice["path"])

    requests.post(setup["update_url"], files={
                  "invoice": setup["updated_invoice"]}, data={"token":setup["token"], "invoice_id": "0"})
    
    invoice = list_v1(setup["token"])[0]
    assert invoice["path"] == "app/invoices_received\\jerrythompson_0.xml"
    assert os.path.getmtime(invoice["path"]) > original_time

def test_access_error_update(setup):
    """
    Error Update Tests
        Checks if update raises AccessError
    """
    with pytest.raises(AccessError):
        response = requests.post(setup["update_url"], files={
                      "invoice": setup["updated_invoice"]}, data={"token":setup["token"], "invoice_id": "-1"})
        process_status_code(response)

    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "0"})

    delete_v1(setup["token"], "0")

    with pytest.raises(AccessError):
        response = requests.post(setup["update_url"], files={
                      "invoice": setup["updated_invoice"]}, data={"token":setup["token"], "invoice_id": "0"})
        process_status_code(response)

def test_payload_error_update(setup):
    """
    Payload Error Tests
        Checks if update raises PayloadError
    """
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "0"})
    
    with pytest.raises(PayloadError):
        response = requests.post(setup["update_url"], files={
                      "invoice": setup["updated_invoice"]}, data={"token":setup["token"], "invoice_id": "gibberish"})
        process_status_code(response)
    
    with pytest.raises(PayloadError):
        response = requests.post(setup["receive_url"], files={
                      "invoice": setup["updated_invoice"]}, data={"token":"bad token", "invoice_id": "0"})
        process_status_code(response)

def test_list_v1(setup):
    """
    Valid list_v1 Tests
        Checks if the list_v1 function works
    """
    assert list_v1(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "0"})
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "1"})
    invoice = list_v1(setup["token"])
    assert len(invoice) == 2

    assert invoice[0]["path"] == "app/invoices_received\\jerrythompson_0.xml"
    assert invoice[0]["id"] == 0
    assert invoice[0]["filename"] == "jerrythompson_0.xml"
    assert invoice[0]["output_format"] == 0
    assert invoice[0]["deleted"] == False
    assert invoice[0]["sender"] == "Jerry Thompson"

    assert invoice[1]["path"] == "app/invoices_received\\jerrythompson_1.xml"
    assert invoice[1]["id"] == 1
    assert invoice[1]["filename"] == "jerrythompson_1.xml"
    assert invoice[1]["output_format"] == 1
    assert invoice[1]["deleted"] == False
    assert invoice[1]["sender"] == "Jerry Thompson"

def test_delete_v1(setup):
    """
    Valid delete_v1 Tests
        Checks if the delete_v1 function works
    """
    assert list_v1(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "0"})
    invoice = list_v1(setup["token"])[0]
    assert invoice["path"] == "app/invoices_received\\jerrythompson_0.xml"

    delete_v1(setup["token"], 0)
    assert list_v1(setup["token"]) == []


def test_format_error_delete_v1(setup):
    """
    Error delete_v1 Tests
        Checks if delete_v1 returns FormatError
    """
    with pytest.raises(FormatError):
        delete_v1("bad token", "0")
    
def test_access_error_delete_v1(setup):
    """
    Error delete_v1 Tests
        Checks if delete_v1 returns AccessError
    """
    assert list_v1(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data={"token":setup["token"], "output_format": "0"})
    invoice = list_v1(setup["token"])[0]
    assert invoice["path"] == "app/invoices_received\\jerrythompson_0.xml"

    with pytest.raises(AccessError):
        delete_v1(setup["token"], "-1")

    delete_v1(setup["token"], "0")
    with pytest.raises(AccessError):
        delete_v1(setup["token"], "0")