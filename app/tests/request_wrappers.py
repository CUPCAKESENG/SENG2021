import requests
import json

from app.src.error import PayloadError, FormatError, AccessError

def process_status_code(response):
    if response.status_code == 406:
        raise PayloadError(description=response.reason)
    elif response.status_code == 417:
        raise FormatError(description=response.reason)
    elif response.status_code == 403:
        raise AccessError(description=response.reason)

    return response.json()

def register_v1(email, password, firstname, lastname):
    response = requests.post("http://localhost:5000/register", json={
        "email": email,
        "password": password,
        "firstname": firstname,
        "lastname": lastname
    })
    process_status_code(response)
    data = response.json()
    return data

def delete_v1(token, invoice_id):
    response = requests.delete("http://localhost:5000/invoice/delete", json={
        "token": token,
        "invoice_id": invoice_id
    })
    process_status_code(response)
    data = response.json()
    return data

def list_v1(token):
    response = requests.get("http://localhost:5000/invoice/list", params={
        "token": token
    })
    process_status_code(response)
    data = response.json()
    return data

def clear_v1():
    requests.delete("http://localhost:5000/clear")
