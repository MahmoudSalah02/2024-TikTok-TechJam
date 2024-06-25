from flask import Flask, jsonify
from flask_restful import Api
from flask_mongoengine import MongoEngine
from flask_cors import CORS

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

    from .routes.idea_routes import IdeaList, IdeaDetail, IdeaVote, IdeaDelete, IdeaDeleteAll
    from .routes.celebrity_routes import CelebrityList, CelebrityDetail

    print("Adding API resources...")
    api.add_resource(CelebrityList, '/celebrities')
    api.add_resource(CelebrityDetail, '/celebrities/<string:id>')

# Idea routes
    api.add_resource(IdeaList, '/celebrities/<string:celebrity_id>/ideas')
    api.add_resource(IdeaDetail, '/celebrities/<string:celebrity_id>/ideas/<string:idea_title>')
    api.add_resource(IdeaVote, '/celebrities/<string:celebrity_id>/ideas/<string:idea_title>/vote')
    api.add_resource(IdeaDelete, '/celebrities/<string:celebrity_id>/ideas/<string:idea_title>')
    api.add_resource(IdeaDeleteAll, '/celebrities/<string:celebrity_id>/ideas/delete_all')

    # Hello, World! route
    @app.route('/hello', methods=['GET'])
    def hello_world():
        return jsonify(message="Hello, World!")

    print("Flask app created.")
    return app


