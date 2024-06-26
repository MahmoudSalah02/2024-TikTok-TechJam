from flask import request, jsonify
from flask_restful import Resource
from app.models.user import User
from flask_jwt_extended import create_access_token

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if User.objects(username=username).first():
            response = jsonify({"message": "User already exists"})
            response.status_code = 400
            return response

        user = User(username=username)
        user.set_password(password)
        user.save()
        response = jsonify({"message": "User registered successfully"})
        response.status_code = 201
        return response

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.objects(username=username).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=str(user.id))
            response = jsonify(access_token=access_token)
            response.status_code = 200
            return response
        response = jsonify({"message": "Invalid credentials"})
        response.status_code = 401
        return response
