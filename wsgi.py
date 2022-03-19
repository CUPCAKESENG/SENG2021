"""
SENG2021 - Group Cupcake
File: wsgi.py
    Description: Runs the Flask server for the invoice receiving API
"""

import sys
import os

from app.main import app

def clear_files(folder):
    for filename in os.listdir(folder):
        if filename == 'a.txt':
            continue

        file_path = os.path.join(folder, filename)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path} due to {e}')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == '--clear' and os.path.exists('app/saves/data.p'):
            os.remove('app/saves/data.p')
            clear_files('app/invoices_received/')
            clear_files('app/communication_report/')
            print('/// Cleared old save files')
            

    app.run()
