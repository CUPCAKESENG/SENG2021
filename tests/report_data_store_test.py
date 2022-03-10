
import os,sys
p = os.path.abspath('../src')
sys.path.append(p)
import pytest
from urllib.request import urlopen
import requests
import report_data_store

p = os.path.abspath('../src')
sys.path.append(p)

def test_file_size_init_zero():
    data_store = report_data_store.Datastore()
    data_store_value = data_store.get()
    assert data_store_value['file_size'] == 0

def test_set_store():
    data_store = report_data_store.Datastore()
    data_store.set( {
        'file_size': 1000,
        'file_name': 'file.txt',
        'file_type': 'txt',
        'sender': 'name',
        'receieved_time': 1,
        'created_time': 1,
        'errors': {}
    })
    updated_data_store = data_store.get()
    assert  updated_data_store['file_size'] == 1000 
    assert  updated_data_store['file_name'] == 'file.txt'
    assert  updated_data_store['file_type'] == 'txt'
    assert  updated_data_store['sender'] == 'name'
    assert  updated_data_store['receieved_time'] == 1
    assert  updated_data_store['created_time'] == 1
    assert  updated_data_store['errors'] == {}
    

# def test_throws_error():
#     data_store = report_data_store.Datastore()
#     with pytest.raises(Exception):
#         data_store.err()


base_url = "localhost:3000"

# test api methods
def test_home():
    "GET request to base route returns a 407"
    path = f"{base_url}/"
    resp = requests.get(path)
    assert resp.status_code == 407

def test_parameters_empty():
    "GET request to base route returns a 407"
    path = f"{base_url}/"
    param = []
    resp = requests.get(path, param)
    assert resp.status_code == 407

def test_format_range():
    "check that the api throws a FormatError 417 when the range in not between [0, 2]"
    path = f"{base_url}/send_invoice"
    payload = {'File.txt': '5'}
    response = requests.post(path, data = payload)
    assert response.status_code == 417

def test_format_not_an_integer():
    "check that the api throws a FormatError 417"
    path = f"{base_url}/send_invoice"
    payload = {'File.txt': '1'}
    response = requests.post(path, data = payload)
    assert response.status_code == 417

