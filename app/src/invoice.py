"""
SENG2021 - Group Cupcake
File: receive.py
    Description: Defines the invoice receive function
"""
import os
from werkzeug.utils import secure_filename

from app.src.error import FormatError, AccessError
from app.src.helpers import decode_token
from app.src.data_store import set_data, get_data


def receive(token, invoice, output_format):
    """
    Invoice Receive function
        Params: token, invoice, output_format
        Returns: {user_id, token}
        Errors: InputError if email or password is incorrect.
    """
    datastore = get_data()
    user_id = decode_token(token)['id']

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

    datastore['users'][user_id]['invoices'].append(save_path)

    return {'message': 'Upload Success'}


def update(token, invoice, output_format):
    """
    Invoice Update function
        Params: invoice, output_format
        Returns: {user_id, token}
        Errors: InputError if email or password is incorrect.
    """
    return {invoice, output_format}


def delete(token, invoice, output_format):
    """
    Invoice Receive function
        Params: invoice, output_format
        Returns: {user_id, token}
        Errors: InputError if email or password is incorrect.
    """
    return {invoice, output_format}
