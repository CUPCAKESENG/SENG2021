"""
SENG2021 - Group Cupcake
File: invoice.py
    Description: Defines the invoice functions
"""
import os
from datetime import datetime
from time import strftime
from werkzeug.utils import secure_filename

from app.src.error import AccessError, FormatError
from app.src.helpers import decode_token
from app.src.data_store import set_data, get_data
from app.src.json_report import create_json_report

def receive(token, invoice, output_format):
    """
    Invoice Receive function
        Params: token, invoice, output_format
        Returns: {communication_report}
        Errors: InputError if email or password is incorrect.
    """
    datastore = get_data()
    user_id = decode_token(token)['id']

    # Is there a situation that this is needed?
    if not(0 <= user_id < len(datastore['users'])):
        raise AccessError('Invalid user ID or token')

    if invoice.content_type != 'application/xml':
        raise FormatError('The invoice must be an XML document')

    try:
        output_format = int(output_format)
    except Exception as e:
        raise FormatError(
            'The output format must be\n\t[0] - JSON\n\t[1] - PDF\n\t[2] - HTML') from e
    
    if output_format not in [0, 1, 2]:
        raise FormatError(
            'The output format must be\n\t[0] - JSON\n\t[1] - PDF\n\t[2] - HTML')

    filename = secure_filename(f"{datastore['users'][user_id]['username']}_{len(datastore['users'][user_id]['invoices'])}.xml")
    save_path = os.path.join('app/invoices_received', filename)
    invoice.save(save_path)
    save_time = datetime.now()

    report = {
        'path': save_path,
        'id': len(datastore['users'][user_id]['invoices']),
        'sender': datastore['users'][user_id]['username'],
        'received_time': save_time.strftime('%m/%d/%Y, %H:%M:%S')
    }

    datastore['users'][user_id]['invoices'].append(report)

    return {'communication_report': create_json_report(report)}


def update(token, updated_invoice, invoice_id):
    """
    Invoice Update function
        Params: invoice_id, output_format
        Returns: {user_id, token}
        Errors: AccessError if token is incorrect or invoice_id is invalid.
    """
    datastore = get_data()
    user_id = decode_token(token)['id']

    if not(0 <= user_id < len(datastore['users'])):
        raise AccessError('Invalid user ID or token')
    



def delete(token, invoice):
    """
    Invoice Delete function
        Params: invoice, output_format
        Returns: {}
        Errors: AccessError if token is incorrect.
    """

def list(token):
    """
    Invoice List Function
        Params: token
        Returns: invoices
        Errors: AccessError if token is incorrect.
    """
    datastore = get_data()
    user_id = decode_token(token)['id']

    if not(0 <= user_id < len(datastore['users'])):
        raise AccessError('Invalid user ID or token')

    for user in datastore["users"]:
        if user["user_id"] == user_id:
            return user["invoices"]
