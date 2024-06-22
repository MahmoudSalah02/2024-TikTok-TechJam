from flask_restful import Resource, reqparse
from app.services.idea_service import IdeaService

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
    def post(self, id):
        print(f"POST /ideas/{id}/vote request received")
        parser = reqparse.RequestParser()
        parser.add_argument('upvote', type=bool, required=True)
        args = parser.parse_args()
        print("Parsed args for voting:", args)
        idea = IdeaService.update_votes(id, upvote=args['upvote'])
        if idea:
            return idea.to_json(), 200
        return {'message': 'Idea not found'}, 404
    
class IdeaDelete(Resource):
    def post(self, id):
        print(f"DELETE /ideas/{id} request received")
        success = IdeaService.delete_idea_by_id(id)
        if success:
            return {'message': f'Idea with ID {id} deleted.'}, 200
        return {'message': 'Idea not found'}, 404
    
class IdeaDeleteAll(Resource):
    def post(self):
        print(f"DELETE /ideas request received")
        success = IdeaService.delete_all_ideas()
        if success:
            return {'message': 'All ideas deleted'}, 200
        return {'message': "Somethings's wrong"}, 404

