from flask import json, jsonify, Response, Blueprint
from app import app

@app.before_request
def before_request():
    pass
    #print request.args

apiView = Blueprint('api', __name__, url_prefix='/api')

@apiView.route('/ping', methods=['GET', 'POST'])
def ping():
    return "pong"
