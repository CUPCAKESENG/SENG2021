"""
SENG2021 - Group Cupcake
File: wsgi.py
    Description: Runs the Flask server for the invoice receiving API
"""

from app.main import APP

if __name__ == "__main__":
    APP.run()
