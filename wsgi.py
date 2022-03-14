"""
SENG2021 - Group Cupcake
File: wsgi.py
    Description: Runs the Flask server for the invoice receiving API
"""

import sys
import os

from app.main import app

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1] == '--clear' and os.path.exists('app/saves/data.p'):
            os.remove('app/saves/data.p')
            print('/// Cleared old save file')

    app.run()
