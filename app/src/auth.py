"""
SENG2021 - Group Cupcake
File: auth.py
    Description: Defines functions for auth server routes
"""

from app.src.data_store import data
from app.src.error import FormatError, AccessError
from app.src.helpers import generate_token, is_valid, hash_password


def register(email, password, firstname, lastname):
    """
    Register function
        Params: email, password, firstname, lastname
        Returns: {user_id, token}
        Errors: FormatError if email is invalid. InputError if user already exists.
    """
    datastore = data
    if not is_valid(email):
        raise FormatError(description='Invalid email ID. Please try again.')

    new_user = {
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'username': firstname + lastname,
        'sessions': [],
    }

    if len(data['users']) > 1:
        for user in datastore['users']:
            if new_user['email'] == user['email']:
                # pylint: disable=C0301
                raise AccessError(description='This email is already registered. Please login instead.')

        new_user['user_id'] = data['users'][-1]['user_id'] + 1
    else:
        new_user['user_id'] = 0

    new_user['password'] = hash_password(password)
    datastore['users'].append(new_user)

    return login(email, password)


def login(email, password):
    """
    Login function
        Params: email, password
        Returns: {user_id, token}
        Errors: InputError if email or password is incorrect.
    """
    for user in data['users']:
        if user['email'] == email:
            if user['password'] == hash_password(password):
                user['sessions'].append(generate_token(user))
                return {
                    'user_id': user['user_id'],
                    'token': user['sessions'][-1]
                }
            raise AccessError(description='Incorrect password, please try again.')
    # pylint: disable=C0301
    raise AccessError(description='This email has not been registered, please register and try again.')


def logout(token):
    """
    Logout function
        Params: token
        Returns: 200 OK
        Errors: InputError if token is incorrect. FormatError if token is not a JWT.
    """

    return {token}
