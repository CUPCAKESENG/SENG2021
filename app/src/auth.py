import re
from hashlib import sha3_512
#from jwt import encode
from src.config import SALT
from src.data_store import data

def register(email, password, last_name, first_name):
    datastore = data
    if not isValid(email):
        return {} # this would be an input error
    new_user = {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'sessions': [],
    }
    if len(data['users']) > 1:
        new_user['user_id'] = data['users'][-1]['user_id'] + 1
    else:
        new_user['user_id'] = 0
    
    new_user['password'] = hash_password(password)
    datastore['users'].append(new_user)
    return new_user



def isValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False

def hash_password(password):
    return sha3_512(f"{password}{SALT}".encode()).hexdigest()