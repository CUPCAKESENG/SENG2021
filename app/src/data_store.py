"""
SENG2021 - Group Cupcake
File: data_store.py
    Description: Defines storage for the server
"""

import time
import pickle

data = {
    'users': []
}


def autosave():
    """
    Autosave function
        Params: N/A
        Returns: N/A
        Errors: N/A
        Description: Pickles datastore every 5 seconds to create a save state.
    """
    global data

    # On program launch, will see if there is a pre-existing save
    try:
        with open('app/saves/data.p', 'rb') as old_save:
            old_data = pickle.load(old_save)
            data = old_data
        print('/// Save file loaded successfully')
    except FileNotFoundError:
        print('!!! No saved save file detected. Please ensure that you are running the server from wsgi.py"')

    while True:
        with open('app/saves/data.p', 'wb+') as new_save:
            pickle.dump(data, new_save)
            # print(f'\nSaved data - {data}\n')  # for debugging
            # print('/// Saved state')

        time.sleep(5)
