"""
SENG2021 - Group Cupcake
File: helpers.py
    Description: Defines helper functions for the server.
"""

import re
from datetime import datetime, timedelta, timezone
from random import randint
from hashlib import sha3_512
import jwt
from app.src.config import SALT, SECRET
from app.src.error import AccessError, FormatError


def generate_token(user):
    """
    Generate Token function
        Params: user object
        Returns: token
        Errors: N/A
    """
    payload = {
        'id': user['user_id'],
        'name': user['username'],
        'wildcard': randint(-8096, 8096),
        # Token expires after 20 minutes
        'exp': datetime.now(tz=timezone.utc) + timedelta(minutes=20)
    }
    token = jwt.encode(payload, SECRET)
    return token


def decode_token(token):
    """
    Decode Token function
        Params: jwt token
        Return: token data
        Errors: AccessError if token is expired,
                FormatError if token is incorrect
    """
    try:
        output = jwt.decode(token, SECRET, algorithms=['HS256'])
        return output
    except jwt.ExpiredSignatureError as timeout:
        raise AccessError('This token has timed out, please login again') from timeout
    except (jwt.InvalidTokenError, jwt.DecodeError) as token_errors:
        raise FormatError(
            'This token is incorrectly formatted') from token_errors


def is_valid(email):
    """
    Checks if email is valid
        Params: email
        Returns: TRUE/FALSE
    """
    regex = re.compile(
        r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

    return re.fullmatch(regex, email)


def hash_password(password):
    """
    Hash Password function
        Params: password
        Returns: hashed password
    """
    return sha3_512(f"{password}{SALT}".encode()).hexdigest()
