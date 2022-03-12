from app.src.data_store import data
from app.src.error import PayloadError, FormatError
from app.src.helpers import generate_token, is_valid, hash_password

def register(email, password, firstname, lastname):
    datastore = data
    if not is_valid(email):
        return {} # this would be an input error
    new_user = {
        'email': email,
        'firstname': firstname,
        'lastname': lastname,
        'username': firstname + lastname,
        'sessions': [],
    }
    if len(data['users']) > 1:
        new_user['user_id'] = data['users'][-1]['user_id'] + 1
    else:
        new_user['user_id'] = 0
    
    new_user['password'] = hash_password(password)
    datastore['users'].append(new_user)

    return login(email, password)

def login(email, password):
    for user in data['users']:
        if user['email'] == email:
            if user['password'] == hash_password(password):
                user['sessions'].append(generate_token(user))
                return {
                    'user_id': user['user_id'],
                    'token': user['sessions'][-1]
                }
            return {} # this would be an input error for wrong email or password
    return {} # this would be an input error for wrong email or password

def logout(email):
    return {}

