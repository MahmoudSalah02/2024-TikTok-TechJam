from flask import Flask, jsonify
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = MongoEngine()

def create_app():
    print("Creating Flask app...")
    app = Flask(__name__)
    print("Loading config...")
    app.config.from_object('config.Config')
    print("Initializing MongoDB...")
    db.init_app(app)
    print("Setting up API...")
    api = Api(app)
    CORS(app)  # Enable CORS for the Flask app
    jwt = JWTManager(app)

    from .routes.idea_routes import IdeaList, IdeaDetail, IdeaVote
    from .routes.auth_routes import UserRegister, UserLogin

    print("Adding API resources...")
    api.add_resource(IdeaList, '/ideas')
    api.add_resource(IdeaDetail, '/ideas/<id>')
    api.add_resource(IdeaVote, '/ideas/<id>/vote')
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')

    # Hello, World! route
    @app.route('/hello', methods=['GET'])
    def hello_world():
        return jsonify(message="Hello, World!")

    print("Flask app created.")
    return app
