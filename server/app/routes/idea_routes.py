from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.idea_service import IdeaService
from app.models.user import User

class IdeaList(Resource):
    def get(self):
        print("GET /ideas request received")
        ideas = IdeaService.get_all_ideas()
        return [idea.to_json() for idea in ideas], 200

    def post(self):
        print("POST /ideas request received")
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('description', required=True)
        args = parser.parse_args()
        print("Parsed args:", args)
        idea = IdeaService.create_idea(args)
        return idea.to_json(), 201

class IdeaDetail(Resource):
    def get(self, id):
        print(f"GET /ideas/{id} request received")
        idea = IdeaService.get_idea_by_id(id)
        if idea:
            return idea.to_json(), 200
        return {'message': 'Idea not found'}, 404

class IdeaVote(Resource):
    @jwt_required()
    def post(self, id):
        print(f"POST /ideas/{id}/vote request received")
        parser = reqparse.RequestParser()
        parser.add_argument('upvote', type=bool, required=True)
        args = parser.parse_args()
        print("Parsed args for voting:", args)

        user_id = get_jwt_identity()
        user = User.objects(id=user_id).first()

        if not user:
            return {'message': 'User not found'}, 404

        if args['upvote']:
            if id in user.upvoted_ideas:
                return {'message': 'User has already upvoted this idea'}, 400
            user.upvoted_ideas.append(id)
            if id in user.downvoted_ideas:
                user.downvoted_ideas.remove(id)
            user.save()
        else:
            if id in user.downvoted_ideas:
                return {'message': 'User has already downvoted this idea'}, 400
            user.downvoted_ideas.append(id)
            if id in user.upvoted_ideas:
                user.upvoted_ideas.remove(id)
            user.save()

        idea = IdeaService.update_votes(id, upvote=args['upvote'])
        if idea:
            return idea.to_json(), 200
        return {'message': 'Idea not found'}, 404
