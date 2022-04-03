"""
SENG2021 - Group Cupcake
File: data_store.py
    Description: Defines storage for the server
"""

import time
import pickle
import os
import jwt

from app.src.config import SECRET

DATA = {
    'users': []
}


def get_data():
    """
    Get Data function
        Params: N/A
        Returns: data
        Errors: N/A
        Description: Gets data in the datastore.
    """

    return DATA


def set_data(updated):
    """
    Set Data function
        Params: json object
        Returns: N/A
        Errors: N/A
        Description: Sets data in the datastore.
    """

    global DATA
    DATA = updated
    with open('app/saves/data.p', 'wb+') as new_save:
        pickle.dump(DATA, new_save)
        # print(f'\n\n/// Save change {DATA} \n') for debugging


def clean_tokens():
    """
    Clean tokens function
        Params: N/A
        Returns: N/A
        Errors: N/A
        Description: Clears tokens that are expired from the data store every 10 minutes.
    """

    time.sleep(60)  # Wait for datastore to be imported
    global DATA

    while True:
        for user in DATA['users']:
            for token in user['sessions']:
                try:
                    jwt.decode(token, SECRET, algorithms=['HS256'])
                except jwt.ExpiredSignatureError as timeout:
                    DATA['users'][user['user_id']
                                       ]['sessions'].remove(token)
                    print(
                        f'\\\\\\ Token {token[:5]} has been cleared due to expiry')

        set_data(DATA)
        time.sleep(10*60)  # Run once every 10 minutes


def autosave():
    """
    Autosave function
        Params: N/A
        Returns: N/A
        Errors: N/A
        Description: Pickles datastore every 5 seconds to create a save state.
    """
    global DATA

    time.sleep(2)  # Let the server startup text show properly
    # On program launch, will see if there is a pre-existing save
    try:
        with open('app/saves/data.p', 'rb') as old_save:
            old_data = pickle.load(old_save)
            set_data(old_data)
        print('/// Save file loaded successfully')
        # print(DATA)
    except FileNotFoundError:
        print('!!! No saved save file detected. Please ensure that any saves are stored in app/saves"')
        if not os.path.exists('app/saves'):
            os.mkdir('app/saves')

    while True:
        with open('app/saves/data.p', 'wb+') as new_save:
            pickle.dump(get_data(), new_save)
            # print(f'\nSaved data - {DATA}\n')  # for debugging
            # print('/// Saved state')

        time.sleep(5)


def clear():
    """
    Clear function
        Params: N/A
        Returns: N/A
        Errors: N/A
        Description: Clears data in data store.
    """
    set_data({"users": []})
