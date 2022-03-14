"""
SENG2021 - Group Cupcake
File: data_store.py
    Description: Defines storage for the server
"""

import time
import pickle
import os
from werkzeug.utils import secure_filename

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

    global DATA
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
            DATA = old_data
        print('/// Save file loaded successfully')
        # print(DATA)
    except FileNotFoundError:
        print('!!! No saved save file detected. Please ensure that you are running the server from wsgi.py"')
        if not os.path.exists('app/saves'):
            os.mkdir('app/saves')

    while True:
        with open('app/saves/data.p', 'wb+') as new_save:
            pickle.dump(DATA, new_save)
            # print(f'\nSaved data - {data}\n')  # for debugging
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
