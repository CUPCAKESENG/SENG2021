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
                        Occurs when received payload has formatting issues.
    """
    code = 406
    message = 'No message specified'


class FormatError(HTTPException):
    """
    FormatError class
        Description: Defines a HTTP response for a FormatError.
                        Occurs when request received is invalid or has formatting issues.
    """
    code = 417
    message = 'No message specified'


class AccessError(HTTPException):
    """
    AccessError class
        Description: Defines a HTTP response for an AccessError.
                        Occurs when user request has authorisation issues.
    """
    code = 403
    message = 'No message specified'
