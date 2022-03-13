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
from app.src.invoice import receive, update, delete

APP = Flask(__name__)

@APP.route("/test", methods=["GET"])
def test():
    """
    Test Route
    """
    return {"message": "testing"}

@APP.route("/register", methods=["POST"])
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

@APP.route('/login', methods=["POST"])
def login_user():
    """
    Login route
        Expected Input Payload: {email, password}
        Returns: {user_id, token}
    """
    info = request.get_json()
    ret = login(info['email'].lower(), info['password'])
    return dumps(ret)

@APP.route("/logout", methods=["POST"])
def logout_user():
    """
    Logout route
        Expected Input Payload: {email, token}
        Returns: {}
    """
    info = request.get_json()
    return dumps(logout(info['token']))

@APP.route("/invoice/receive", methods=["POST"])
def invoice_receive():
    """
    Receive route
        Expected Input Payload: {invoice}
        Returns: {communication_report}
    """
    try:
        invoice = request.files['invoice']
        token = request.form['token']
        output_format = request.form['output_format']
    except:
        raise PayloadError('Invalid receipt request')

    info = request.get_json()
    ret = receive(info['token'], info['invoice'], info['output_format'])
    return dumps(ret)

persist = threading.Thread(target=autosave, daemon=True)
persist.start()

# if __name__ == "__main__":
#     APP.run()
