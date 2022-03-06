from flask import Flask, request
import json
from json import dumps

APP = Flask(__name__)

@APP.route("/invoice/receive", methods=["POST"])
def receive():
    info = request.get_json()
    ret = invoice_receive(info['invoice'], info['output-format'])
    return dumps({
        'output_report': ret['output-format']
    })

if __name__ == "__main__":
    APP.run()