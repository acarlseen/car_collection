'''
helps with other functions and users login correctly and that users have right to access API data

check tokens for rightful access to content
api will be rules for contacts stored, etc
'''

from functools import wraps
import secrets
from flask import request, jsonify, json
import decimal
import json

from models import User

# below is kinda boiler plate
def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1] #interactis with 'insomnia'
        if not token:
            return jsonify({'message': 'Token is missing.'}), 401
        
        try:
            current_user_token = User.query.filter_by(token = token).first()
            # taking token from request, saving to 'token', search for user with that token in the database
            print(token)
            print(current_user_token)
        except:
            owner = User.query.filter_by(token = token).first()

            if token != owner.token and secrets.compare_digest():
                return jsonify({'message': 'Token is invalid'})
        return our_flask_function(current_user_token, *args, **kwargs)  #all functions that use this decorator wilil need
                                                                        # current_user_token as a first positional argument
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)