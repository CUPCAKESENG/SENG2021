"""
SENG2021 - Group Cupcake
File: receive.py
    Description: Defines the invoice receive function
"""

from app.src.error import AccessError
from app.src.helpers import decode_token
from app.src.data_store import set_data, get_data


def receive(token, invoice, output_format):
    """
    Invoice Receive function
        Params: invoice, output_format
        Returns: {user_id, token}
        Errors: InputError if email or password is incorrect.
    """
    datastore = get_data()
    user_id = decode_token(token)['id']

    if not(0 <= user_id < len(datastore['users'])):
        raise AccessError('Invalid user ID or token')

    datastore['users'][user_id]['invoices'].append()

    return {invoice, output_format}


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
