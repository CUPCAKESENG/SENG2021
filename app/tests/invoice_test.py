"""
SENG2021 - Group Cupcake
File: invoice_test.py
    Description: Static tests for invoice_test.py code
"""

from ast import For
import sys
import os
from app.src.error import AccessError, FormatError
import pytest
import requests
# from app.src.data_store import data

from app.src.auth import register, is_valid
from app.src.data_store import clear
from app.src.invoice import delete, receive, update, list
# not sure how to properly Import  -> this is a temporary solution
sys.path.insert(0, '..')


@pytest.fixture
def setup():
    clear()
    token = register("owner@streams.com.au", "i am the owner",
                     "Jerry", "Thompson")["token"]
    invoice = open("app/invoices_received/sample.xml", "r")
    wrong_format = open("app/invoices_received/a.txt", "r")
    updated_invoice = open("app/tests/files/updated_invoice.xml", "r")
    wrong_format_2 = open("app/tests/files/b.txt", "r")
    receive_url = "http://localhost:5000/invoice/receive"
    update_url = "http://localhost:5000/invoice/update"
    delete_url = "http://localhost:5000/invoice/delete"

    return {
        "token": token,
        "invoice": invoice,
        "wrong_format": wrong_format,
        "wrong_format_2": wrong_format_2,
        "updated_invoice": updated_invoice,
        "receive_url": receive_url,
        "update_url": update_url,
        "delete_url": delete_url
    }


def test_receive(setup):
    """
    Valid Receive Tests
        Checks if the receive function works
    """
    data = {"token":setup["token"], "output_format": "0"}
    assert list(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, data=data)
    comparison = [{"file_name": "jerrythompson_0"}]
    assert list(setup["token"]) == comparison

def test_format_error_receive(setup):
    """
    Error Receive Tests
        Checks if receive raises FormatError
    """
    with pytest.raises(FormatError):
        requests.post(setup["receive_url"], files={
                      "invoice": setup["wrong_format"]}, token=setup["token"], output_format="0")

    with pytest.raises(FormatError):
        requests.post(setup["receive_url"], files={
                      "invoice": setup["invoice"]}, token=setup["token"], output_format=0)

    with pytest.raises(FormatError):
        requests.post(setup["receive_url"], files={
                      "invoice": setup["invoice"]}, token=setup["token"], output_format="4")


def test_access_error_receive(setup):
    """
    Error Receive Tests
        Checks if receive raises AccessError
    """
    with pytest.raises(AccessError):
        requests.post(setup["receive_url"], files={
                      "invoice": setup["invoice"]}, token="bad token", output_format="0")


def test_update(setup):
    """
    Valid Update Tests
        Checks if the update function works
    """
    assert list(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "new_invoice": setup["invoice"]}, token=setup["token"], output_format="0")
    original_time = os.path.getmtime("app/invoices_received/jerrythompson_1")
    assert list(setup["token"]) == ["app/invoices_received/jerrythompson_1"]

    requests.post(setup["update_url"], files={
                  "invoice": setup["updated_invoice"]}, token=setup["token"], invoice_id=0)
    assert list(setup["token"]) == ["app/invoices_received/jerrythompson_1"]
    assert os.path.getmtime(
        "app/invoices_received/jerrythompson_1") > original_time


def test_format_error_update(setup):
    """
    Error Update Tests
        Checks if update returns FormatError
    """
    with pytest.raises(FormatError):
        requests.post(setup["update_url"], files={
                      "invoice": setup["updated_invoice"]}, token=setup["token"], invoice_id=-1)

    with pytest.raises(FormatError):
        requests.post(setup["update_url"], files={
                      "invoice": setup["updated_invoice"]}, token=setup["token"], invoice_id="gibberish")

    with pytest.raises(FormatError):
        requests.post(setup["update_url"], files={
                      "invoice": setup["wrong_format_2"]}, token=setup["token"], invoice_id="0")


def test_access_error_update(setup):
    """
    Error Update Tests
        Checks if update raises AccessError
    """
    with pytest.raises(AccessError):
        requests.post(setup["receive_url"], files={
                      "invoice": setup["updated_invoice"]}, token="bad token", invoice_id="0")


def test_list(setup):
    """
    Valid List Tests
        Checks if the list function works
    """
    assert list(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, token=setup["token"], output_format="0")
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, token=setup["token"], output_format="0")
    assert len(list(setup["token"])) == 2
    assert list(setup["token"]) == [
        "app/invoices_received/jerrythompson_1", "app/invoices_received/jerrythompson_2"]


def test_access_error_list(setup):
    """
    Error List Tests
        Checks if list returns AccessError
    """
    with pytest.raises(AccessError):
        list("bad token")


def test_delete(setup):
    """
    Valid Delete Tests
        Checks if the delete function works
    """
    assert list(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, token=setup["token"], output_format="0")
    assert list(setup["token"]) == ["/jerrythompson_1"]

    requests.post(setup["delete_url"], files={
                  "invoice": setup["invoice"]}, token=setup["token"])
    assert list(setup["token"]) == []


def test_format_error_delete(setup):
    """
    Error Delete Tests
        Checks if delete returns FormatError
    """
    assert list(setup["token"]) == []
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, token=setup["token"], output_format="0")
    assert list(setup["token"]) == ["/jerrythompson_1"]

    with pytest.raises(FormatError):
        requests.post(setup["delete_url"], files={
                      "invoice": setup["wrong_format"]}, token=setup["token"])


def test_access_error_delete(setup):
    """
    Error Delete Tests
        Checks if delete returns AccessError
    """
    requests.post(setup["receive_url"], files={
                  "invoice": setup["invoice"]}, token=setup["token"], output_format="0")

    with pytest.raises(AccessError):
        requests.post(setup["delete_url"], files={
                      "invoice": setup["invoice"]}, token="bad token")
