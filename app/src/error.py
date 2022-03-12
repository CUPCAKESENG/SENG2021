"""
SENG2021 - Group Cupcake
File: error.py
    Description: Defines HTTP error types for server
"""

from werkzeug.exceptions import HTTPException


class PayloadError(HTTPException):
    """
    PayloadError class
        Description: Defines a HTTP response for a PayloadError.
    """
    code = 406
    message = 'No message specified'


class FormatError(HTTPException):
    """
    FormatError class
        Description: Defines a HTTP response for a FormatError.
    """
    code = 417
    message = 'No message specified'
