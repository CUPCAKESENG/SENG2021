import sys
sys.path.insert(0, '..')   # not sure how to properly Import  -> this is a temporary solution
from src.auth import register, isValid, hash_password

def testValidEmail():
  testEmail = "testEmail@hotmail.com"
  testResult = isValid(testEmail)
  assert testResult == True

def testInvalidEmail():
  testEmail = "123testEmailhotmail.com"
  testResult = isValid(testEmail)
  assert testResult == False




testValidEmail()
testInvalidEmail()





