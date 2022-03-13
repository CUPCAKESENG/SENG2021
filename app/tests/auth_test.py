"""
SENG2021 - Group Cupcake
File: auth_test.py
    Description: Static tests for auth.py code
"""
import pytest
from app.src.error import AccessError, FormatError
from app.src.data_store import clear
from app.src.auth import register, is_valid, login, logout

@pytest.fixture
def register_user():
    clear()
    register('inigomontoyaaa@test.com', 'you_k1ll3d_my_f4th3r', 'inaaigo', 'aamontoya')
    user = register('inigomontoya@test.com', 'you_k1ll3d_my_f4th3r', 'inigo', 'montoya')

    register('inigaaaaaaomontoyaaa@test.com', 'you_k1ll3d_my_f4th3r', 'inaaaigo', 'aamontoya')
    return user


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
    with pytest.raises(FormatError):
        assert(register('123', 'hahahah', 'aaa', 'aaaaaa'))
    
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
    user = register(test_email, test_password, test_firstname, test_lastname)
    assert('user_id' in user.keys())
    assert('token' in user.keys())


def test_incorrect_password(register_user):
    user = register_user
    with pytest.raises(AccessError):
        assert(login('inigomontoya@test.com', 'akjlsndkjasnf'))


