from flask import json 
from werkzeug.exceptions import HTTPException 

class PayloadError(HTTPException):
    code = 406
    message = 'No message specified'

class FormatError(HTTPException):
    code = 417
    message = 'No message specified'
