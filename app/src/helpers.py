"""
SENG2021 - Group Cupcake
File: helpers.py
    Description: Defines helper functions for the server.
"""

import re
from random import randint
from hashlib import sha3_512
from jwt import encode
from app.src.config import SALT, SECRET


def generate_token(user):
    """
    Generate Token function
        Params: user object
        Returns: token
        Errors: N/A
    """
    payload = {
        'sub': user['user_id'],
        'name': user['username'],
        'wildcard': randint(-8096, 8096)
    }
    token = encode(payload, SECRET)
    return token


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
