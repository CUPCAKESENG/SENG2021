from flask import Flask#, request
#import json
#from json import dumps

#from src.auth import register, login, logout



APP = Flask(__name__)

@APP.route("/")
def home():
  return "<h1>Testing</h1>"

# @APP.route("/test", methods=["GET"])
# def test():
#   return {"message": "testing"}

# @APP.route("/register", methods=["POST"])
# def register():
#     info = request.get_json()
#     ret = register(info['email'], info['password'], info['first_name'], info['last_name'])
#     return dumps({
#         'token': ret['token'],
#     })

# @APP.route('/login', methods=["POST"])
# def login():
#     info = request.get_json()
#     ret = login(info['email'], info['password'])
#     return dumps({
#         'token': ret['token'],
#     })

# @APP.route("/logout", methods=["POST"])
# def logout():
#     info = request.get_json()
#     logout(info['token'])
#     return dumps({

#     })    

# @APP.route("/invoice/receive", methods=["POST"])
# def receive():
#     info = request.get_json()
#     ret = invoice_receive(info['invoice'], info['output-format'])
#     return dumps({
#         'output_report': ret['output-format'],
#         'invoice_id': ret['id'],
#     })



# if __name__ == "__main__":
#     APP.run()