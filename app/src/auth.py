"""
SENG2021 - Group Cupcake
File: auth.py
    Description: Defines functions for auth server routes
"""

from app.src.data_store import get_data, set_data
from app.src.error import FormatError, AccessError
from app.src.helpers import decode_token, generate_token, is_valid, hash_password


def register(email, password, firstname, lastname):
    """
    Register function
        Params: email, password, firstname, lastname
        Returns: {user_id, token}
        Errors: FormatError if email is invalid. InputError if user already exists.
    """
    datastore = get_data()
    if not is_valid(email):
        raise FormatError('Invalid email ID. Please try again.')

    new_user = {
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'username': firstname + lastname,
        'sessions': [],
        'invoices': [],
        'graph': []
    }

    for user in datastore['users']:
        if new_user['email'] == user['email']:
            raise AccessError(
                'This email is already registered. Please login or register a different email.')

    new_user['user_id'] = len(datastore['users'])

    new_user['password'] = hash_password(password)
    datastore['users'].append(new_user)
    set_data(datastore)

    return login(email, password)


def login(email, password):
    """
    Login function
        Params: email, password
        Returns: {user_id, token}
        Errors: InputError if email or password is incorrect.
    """
    datastore = get_data()

    for user in datastore['users']:
        if user['email'] == email:
            if user['password'] == hash_password(password):
                user['sessions'].append(generate_token(user))

                set_data(datastore)

                return {
                    'user_id': user['user_id'],
                    'token': user['sessions'][-1]
                }
            raise AccessError('Incorrect password, please try again.')
    raise AccessError(
        'This email has not been registered, please register and try again.')


def logout(token):
    """
    Logout function
        Params: token
        Returns: N/A
        Errors: AccessError if token is timed out or already logged out.
                FormatError if token is incorrect.
    """
    datastore = get_data()
    details = decode_token(token)

    if token in datastore['users'][details['id']]['sessions']:
        datastore['users'][details['id']]['sessions'].remove(token)
    else:
        raise AccessError('This session token has already been logged out')

    set_data(datastore)
    return {'message': 'Logout successful!'}
