from flask import Flask, jsonify
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_jwt_extended import JWTManager

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    api = Api(app)
    CORS(app)  # Enable CORS for the Flask app
    jwt = JWTManager(app)

    from .routes.idea_routes import IdeaList, IdeaDetail, IdeaVote, IdeaDone
    from .routes.celebrity_routes import CelebrityList, CelebrityDetail
    from .routes.auth_routes import UserRegister, UserLogin

    
    api.add_resource(UserLogin, '/login')
    api.add_resource(UserRegister, '/register')

    api.add_resource(CelebrityList, '/celebrities')
    api.add_resource(CelebrityDetail, '/celebrities/<string:id>')

    api.add_resource(IdeaList, '/celebrities/<string:celebrity_id>/ideas')
    api.add_resource(IdeaDetail, '/celebrities/<string:celebrity_id>/ideas/<string:idea_id>')
    api.add_resource(IdeaVote, '/celebrities/<string:celebrity_id>/ideas/<string:idea_id>/vote')
    api.add_resource(IdeaDone, '/celebrities/<string:celebrity_id>/ideas/<string:idea_id>/done')

    return app
