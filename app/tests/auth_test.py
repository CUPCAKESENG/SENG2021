"""
SENG2021 - Group Cupcake
File: auth_test.py
    Description: Static tests for auth.py code
"""

import sys
# from app.src.data_store import data

from app.src.auth import register, is_valid
# not sure how to properly Import  -> this is a temporary solution
sys.path.insert(0, '..')


def test_valid_email():
    """
    Valid Email Tests
        Checks if the is_valid function works
    """
    assert is_valid('test@email.com')


def test_invalid_emails():
    """
    Invalid Email Tests
        Checks if the is_valid function works
    """
    assert not is_valid('123')
    assert not is_valid('abc')
    assert not is_valid('123@@@')
    assert not is_valid('.com.com')
    assert not is_valid('123testEmailhotmail.com')


def test_valid_registration():
    """
    Valid Registration Tests
        Checks if the register function works
    """
    valid_user = {
        'email': 'john.doe@gmail.com',
        'first_name': 'John',
        'last_name': 'Doe',
        'sessions': [],
        'user_id': 1,
        'username': 'johndoe'
    }

    test_email = 'john.doe@gmail.com'
    test_password = '123'
    test_firstname = 'John'
    test_lastname = 'Doe'

    registered_user = register(
        test_email, test_password, test_firstname, test_lastname)
    print(registered_user, valid_user)
    #self.assertEqual(registered_user, )


test_valid_email()
test_invalid_emails()
test_valid_registration()
