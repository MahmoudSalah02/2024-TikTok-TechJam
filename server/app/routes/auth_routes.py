from flask import request, jsonify
from flask_restful import Resource
from app.models.user import User
from flask_jwt_extended import create_access_token

import logging

logging.basicConfig(level=logging.DEBUG)

class UserRegister(Resource):
    def post(self):
        logging.debug("Received request for user registration")
        data = request.get_json()
        logging.debug(f"Request data: {data}")
        username = data.get('username')
        password = data.get('password')

        if User.objects(username=username).first():
            logging.debug("User already exists")
            return jsonify({"message": "User already exists"}), 400

        user = User(username=username)
        user.set_password(password)
        user.save()
        logging.debug("User registered successfully")
        return jsonify({"message": "User registered successfully"}), 201

class UserLogin(Resource):
    def post(self):
        logging.debug("Received request for user login")
        data = request.get_json()
        logging.debug(f"Request data: {data}")
        username = data.get('username')
        password = data.get('password')

        user = User.objects(username=username).first()
        if user and user.check_password(password):
            logging.debug("User authenticated successfully")
            access_token = create_access_token(identity=str(user.id))
            return jsonify(access_token=access_token), 200
        logging.debug("Invalid credentials")
        return jsonify({"message": "Invalid credentials"}), 401
