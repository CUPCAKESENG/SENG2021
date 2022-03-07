import sys
sys.path.insert(0, '..')   # not sure how to properly Import  -> this is a temporary solution
from src.auth import register, isValid, hash_password
from src.data_store import data


def testValidEmail():
  testEmail = "testEmail@hotmail.com"
  testResult = isValid(testEmail)
  assert testResult == True

def testInvalidEmail():
  testEmail = "123testEmailhotmail.com"
  testResult = isValid(testEmail)
  assert testResult == False

def testValidRegisterDetails():
  testValidUser = {
    'email': "testValidEmail@gmail.com",
    'first_name': "John",
    'last_name': "Doe",
    'sessions': [],
  }
  testEmail = "testValidEmail@gmail.com"
  testPassword = "123"
  testLastName = "Doe"
  testFirstName = "John"

  registeredUser = register(testEmail, testPassword, testLastName, testFirstName)
  #self.assertEqual(registeredUser, )
  





testValidEmail()
testInvalidEmail()
testValidRegisterDetails()





