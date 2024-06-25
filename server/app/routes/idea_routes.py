from flask_restful import Resource, reqparse
from app.services.idea_service import IdeaService

class IdeaList(Resource):
    def get(self, celebrity_id):
        print("GET /celebrities/{celebrity_id}/ideas request received")
        ideas = IdeaService.get_all_celebrity_ideas(celebrity_id)
        return [idea.to_json() for idea in ideas], 200

    def post(self, celebrity_id):
        print("POST /celebrities/{celebrity_id}/ideas request received")
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('description', required=True)
        args = parser.parse_args()
        print("Parsed args:", args)
        idea = IdeaService.add_idea_to_celebrity(celebrity_id, args)
        return idea.to_json(), 201

class IdeaDetail(Resource):
    def get(self, celebrity_id, idea_title):
        print(f"GET /celebrities/{celebrity_id}/ideas/{idea_title} request received")
        idea = IdeaService.get_idea_in_celebrity(celebrity_id, idea_title)
        if idea:
            return idea.to_json(), 200
        return {'message': 'Idea not found'}, 404

class IdeaVote(Resource):
    def post(self, celebrity_id, idea_title):
        print(f"POST /celebrities/{celebrity_id}/ideas/{idea_title}/vote request received")
        parser = reqparse.RequestParser()
        parser.add_argument('upvote', type=bool, required=True)
        args = parser.parse_args()
        print("Parsed args for voting:", args)
        idea = IdeaService.update_celebrity_idea_votes(celebrity_id, idea_title, upvote=args['upvote'])
        if idea:
            return idea.to_json(), 200
        return {'message': 'Idea not found'}, 404

class IdeaDelete(Resource):
    def delete(self, celebrity_id, idea_title):
        print(f"DELETE /celebrities/{celebrity_id}/ideas/{idea_title} request received")
        success = IdeaService.delete_idea_by_id(celebrity_id, idea_title)
        if success:
            return {'message': f'Idea with title {idea_title} deleted.'}, 200
        return {'message': 'Idea not found'}, 404

class IdeaDeleteAll(Resource):
    def delete(self, celebrity_id):
        print(f"DELETE /celebrities/{celebrity_id}/ideas request received")
        deleted_count = IdeaService.delete_all_ideas_from_celebrity(celebrity_id)
        if deleted_count > 0:
            return {'message': f'All {deleted_count} ideas deleted successfully.'}, 200
        return {'message': 'Celebrity not found or no ideas to delete.'}, 404
