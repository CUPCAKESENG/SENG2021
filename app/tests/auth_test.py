import sys
sys.path.insert(0, '..')   # not sure how to properly Import  -> this is a temporary solution
from src.auth import register, is_valid, hash_password
from src.data_store import data


def test_valid_email():
  assert is_valid('test@email.com')

def test_invalid_emails():
  assert !is_valid('123')
  assert !is_valid('abc')
  assert !is_valid('123@@@')
  assert !is_valid('.com.com')
  assert !is_valid('123testEmailhotmail.com')

def test_valid_registration():
  valid_user = {
    'email': 'john.doe@gmail.com',
    'first_name': 'John',
    'last_name': 'Doe',
    'sessions': [],
    'user_id' : 1
    'username' : 'johndoe'
  }

  test_email = 'john.doe@gmail.com'
  test_password = '123'
  test_firstnaame = 'John'
  test_lastname = 'Doe'

  registeredUser = register(test_email, test_password, test_firstname, test_lastname)
  #self.assertEqual(registeredUser, )
  





test_valid_email()
test_invalid_emails()
test_valid_registration()





