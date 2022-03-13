import pytest
from app.src.data_store import clear
from app.src.error import FormatError, AccessError
from app.src.auth import register, logout, login
from app.src.helpers import generate_token, decode_token, hash_password, is_valid


@pytest.fixture
def register_user():
    clear()
    user = register('inigomontoya@test.com', 'you_k1ll3d_my_f4th3r', 'inigo', 'montoya')
    return user


def test_generate_decode_token(register_user):
    user = register_user
    token = login('inigomontoya@test.com', 'you_k1ll3d_my_f4th3r')
#    logout(user['token'])
#    token = generate_token(user)
    print(token['token'])
    token_txt = token['token']
    decoded = decode_token(token_txt) 
    assert("id" in decoded.keys())
    assert("name" in decoded.keys())
    assert("wildcard" in decoded.keys())
    assert("exp" in decoded.keys()) 


def test_logged_out_token(register_user): 
    user = register_user
    logout(user['token']);
    assert(decode_token(user['token']))


def test_invalid_format_token():
    with pytest.raises(FormatError):
        assert(decode_token('aaaaaaaaaaaaaaaaaaaa'))


def test_hashing():
    assert(hash_password('correcthorse') == hash_password('correcthorse'))


def test_is_valid():
    assert(is_valid('test@test.com'))
    assert(is_valid('aaa') == None)
