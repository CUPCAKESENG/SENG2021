


"""
SENG2021 - Group Cupcake
File: main.py
    Description: Defines routes for the server
"""

import threading
from json import dumps
from flask import Flask, render_template, request, send_from_directory
from flask_cors import CORS
# import json

from app.src.data_store import autosave, clean_tokens, clear
from app.src.auth import register, login, logout
from app.src.error import PayloadError
from app.src.invoice import receive, update, delete, list
from app.src.data_store import get_data
from app.src.helpers import decode_token
from app.src.error import AccessError

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/<path:path>')
def send_html(path):
    if path in ['index.html', 'login.html', 'register.html', 'table.html', 'error.html']:
        return render_template(path)
    else:
        return render_template('404.html')

@app.route('/invoice/<path:filename>')
def download_invoice(filename):
    return send_from_directory('invoices_received/', filename, as_attachment=True)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory('templates/assets/', path)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/test", methods=["GET"])
def test():
    """
    Test Route
    """
    return {"message": "testing"}


@app.route("/register", methods=["GET", "POST"])
def register_user():
    """
    Register route
        Expected Input Payload: {email, password, firstname, lastname}
        Returns: {user_id, token}
    """
    if request.method == 'POST':
        new_user = request.get_json()
        ret = register(new_user['email'].lower(), new_user['password'],
                    new_user['firstname'].lower(), new_user['lastname'].lower())
        return dumps(ret)
    else:
        return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login_user():
    """
    Login route
        Expected Input Payload: {email, password}
        Returns: {user_id, token}
    """
    if request.method == 'POST':
        info = request.get_json()
        ret = login(info['email'].lower(), info['password'])
        return dumps(ret)
    else:
        return render_template('login.html')


@app.route("/logout", methods=["POST"])
def logout_user():
    """
    Logout route
        Expected Input Payload: {email, token}
        Returns: {}
    """
    info = request.get_json()
    return dumps(logout(info['token']))

@app.route("/user/graph", methods=["GET"])
def fetch_data():
    """
    Graph Data route
        Expected Input Payload: {token}
        Returns: {List of tuples with cost information}

        Each datapoint is in the format:
            (filename, filesize, received_time, save_time, currency, amount, sender)
    """

    token = request.args.get('token')
    datastore = get_data()
    user_id = decode_token(token)['id']

    if not user_id in range(len(datastore['users'])):
        raise AccessError('Invalid user ID or token')

    response = datastore['users'][user_id]['graph']
    return dumps(response)

@app.route("/user/name", methods=["GET"])
def fetch_name():
    """
    Graph Data route
        Expected Input Payload: {token}
        Returns: {name}
    """

    token = request.args.get('token')
    datastore = get_data()
    user_id = decode_token(token)['id']

    if not user_id in range(len(datastore['users'])):
        raise AccessError('Invalid user ID or token')

    response = {
        'name': f"{datastore['users'][user_id]['firstname'].capitalize()} {datastore['users'][user_id]['lastname'].capitalize()}"
    }
    return dumps(response)

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
    
    if output_format != 0:
        return ret
    else:
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

@app.route("/invoice/delete", methods=["DELETE"])
def invoice_delete():
    """
    Delete route
        Expected Input Payload: {token, invoice_id}
        Returns: {message}
    """
    info = request.get_json()
    try:
        info['invoice_id'] = int(info['invoice_id'])
    except ValueError as not_an_int:
        raise PayloadError('invoice_id must be an integer!') from not_an_int

    return dumps(delete(info['token'], info['invoice_id']))

@app.route("/invoice/list", methods=["GET"])
def invoice_list():
    """
    Logout route
        Expected Input Payload: {token}
        Returns: {message}
    """
    token = request.args.get('token')
    response = list(token)
    return dumps(response)

@app.route("/clear", methods=["DELETE"])
def user_clear():
    return dumps(clear())

persist = threading.Thread(target=autosave, daemon=True)
persist.start()

cleanup = threading.Thread(target=clean_tokens, daemon=True)
cleanup.start()

# if __name__ == "__main__":
#     app.run()
