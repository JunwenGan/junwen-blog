from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from db import db
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import re
register_parser = reqparse.RequestParser()
register_parser.add_argument('username', required=True, help="Username is required")
register_parser.add_argument('email', required=True, help="Email is required")
register_parser.add_argument('password', required=True, help="Password is required")

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True, help="Username is required")
login_parser.add_argument('password', required=True, help="Password is required")


class LoginResource(Resource):
    def post(self):
        args = login_parser.parse_args()
        username = args['username']
        password = args['password']

        user = db.users.find_one({"username": username})
        if not user:
            return {"msg": "Invalid username or password"}, 401

        if not check_password_hash(user['password'], password):
            return {"msg": "Invalid username or password"}, 401
        
        access_token = create_access_token(identity=str(user["_id"]))
        # return jsonify(access_token=access_token)
        return {"access_token": access_token}
    
class RegisterResource(Resource):
    def post(self):
        args = register_parser.parse_args()
        username = args['username']
        email = args['email']
        password =  args['password']

        # check if user existed
        if db.users.find_one({"username": username}):
            return {"msg": "Username already exists"}, 400
        # check password
        if len(password) < 5:
            return {"msg": "Password must be at least 5 characters long"}, 400
        # check email
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(email_regex, email):
            return {"msg": "Invalid email format"}, 400
        
        # create new user
        hashed_password = generate_password_hash(password)
        new_user = {
            "username": username,
            "email": email,
            "password": hashed_password
        }
        db.users.insert_one(new_user)
        return {"msg": "User registered successfully!"}, 201

