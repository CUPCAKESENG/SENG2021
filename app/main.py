from flask import Flask, request
import json
from json import dumps

from app.src.auth import register, login, logout

APP = Flask(__name__)

@APP.route("/test", methods=["GET"])
def test():
  return {"message": "testing"}

@APP.route("/register", methods=["POST"])
def register_user():
	new_user = request.get_json()
	ret = register(new_user['email'].lower(), new_user['password'], new_user['firstname'].lower(), new_user['lastname'].lower())
	return dumps({
		'token': ret['token'],
	})

@APP.route('/login', methods=["POST"])
def login_user():
	info = request.get_json()
	ret = login(info['email'].lower(), info['password'])
	return dumps({
		'token': ret['token'],
	})

@APP.route("/logout", methods=["POST"])
def logout_user():
	info = request.get_json()
	logout(info['token'])
	return dumps({

	})    

@APP.route("/invoice/receive", methods=["POST"])
def receive():
	info = request.get_json()
	ret = invoice_receive(info['invoice'], info['output_format'])
	return dumps({
		'output_report': ret['output_format'],
		'invoice_id': ret['id'],
	})



# if __name__ == "__main__":
#     APP.run()