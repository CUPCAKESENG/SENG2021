import re
from hashlib import sha3_512
from jwt import encode
from app.src.config import SALT, SECRET

def generate_token(user):
    payload = {
        'sub': user['user_id'],
        'name': user['username'],
    }
    token = encode(payload, SECRET)
    return token

def is_valid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def hash_password(password):
    return sha3_512(f"{password}{SALT}".encode()).hexdigest()