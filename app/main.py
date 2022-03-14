"""
SENG2021 - Group Cupcake
File: main.py
    Description: Defines routes for the server
"""

import threading
from json import dumps
from flask import Flask, request
# import json

from app.src.data_store import autosave
from app.src.auth import register, login, logout
from app.src.error import PayloadError
from app.src.invoice import receive, update, delete, list

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test():
    """
    Test Route
    """
    return {"message": "testing"}


@app.route("/register", methods=["POST"])
def register_user():
    """
    Register route
        Expected Input Payload: {email, password, firstname, lastname}
        Returns: {user_id, token}
    """
    new_user = request.get_json()
    ret = register(new_user['email'].lower(), new_user['password'],
                   new_user['firstname'].lower(), new_user['lastname'].lower())
    return dumps(ret)


@app.route('/login', methods=["POST"])
def login_user():
    """
    Login route
        Expected Input Payload: {email, password}
        Returns: {user_id, token}
    """
    info = request.get_json()
    ret = login(info['email'].lower(), info['password'])
    return dumps(ret)


@app.route("/logout", methods=["POST"])
def logout_user():
    """
    Logout route
        Expected Input Payload: {email, token}
        Returns: {}
    """
    info = request.get_json()
    return dumps(logout(info['token']))


@app.route("/invoice/receive", methods=["POST"])
def invoice_receive():
    """
    Receive route
        Expected Input Payload: {token, invoice, output_format}
        Returns: {communication_report}
    """
    try:
        token = request.form['token']
        invoice = request.files['invoice']
        output_format = request.form['output_format']
    except Exception as e:
        raise PayloadError(
            'Invalid receipt request, please send token, invoice and output_format as form fields') from e

    ret = receive(token, invoice, output_format)
    return dumps(ret)

@app.route("/invoice/update", methods=["POST"])
def invoice_update():
    """
    Receive route
        Expected Input Payload: {token, invoice, invoice_id}
        Returns: {communication_report}
    """
    try:
        token = request.form['token']
        invoice = request.files['invoice']
        invoice_id = request.form['invoice_id']
    except Exception as e:
        raise PayloadError(
            'Invalid receipt request, please send token, invoice and invoice_id as form fields') from e

    try:
        invoice_id = int(invoice_id)
    except ValueError as not_an_int:
        raise PayloadError('invoice_id must be an integer!') from not_an_int

    ret = update(token, invoice, invoice_id)
    return dumps(ret)

@app.route("/invoice/delete", methods=["POST"])
def invoice_delete():
    """
    Delete route
        Expected Input Payload: {token, invoice_id}
        Returns: {message}
    """
    info = request.get_json()

    try:
        info['invoice_id'] = info['invoice_id']
    except ValueError as not_an_int:
        raise PayloadError('invoice_id must be an integer!') from not_an_int

    return dumps(delete(info['token'], info['invoice_id']))

@app.route("/invoice/list", methods=["POST"])
def invoice_list():
    """
    Logout route
        Expected Input Payload: {token}
        Returns: {message}
    """
    info = request.get_json()
    return dumps(list(info['token']))

persist = threading.Thread(target=autosave, daemon=True)
persist.start()

# if __name__ == "__main__":
#     app.run()
