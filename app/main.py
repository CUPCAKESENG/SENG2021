"""
SENG2021 - Group Cupcake
File: main.py
    Description: Defines routes for the server
"""

from json import dumps
from flask import Flask, request
import threading
# import json

from app.src.data_store import autosave
from app.src.auth import register, login, logout
from app.src.receive import invoice_receive

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
    logout(info['token'])
    return dumps({

    })

@APP.route("/invoice/receive", methods=["POST"])
def receive():
    """
    Receive route
        Expected Input Payload: {invoice}
        Returns: {communication_report}
    """
    info = request.get_json()
    ret = invoice_receive(info['invoice'], info['output_format'])
    return dumps(ret)

persist = threading.Thread(target=autosave, daemon=True)
persist.start()

# if __name__ == "__main__":
#     APP.run()
