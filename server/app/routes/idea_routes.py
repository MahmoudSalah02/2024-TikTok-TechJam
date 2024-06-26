from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.idea_service import IdeaService
from app.models.user import User

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
    def get(self, celebrity_id, idea_id):
        print(f"GET /celebrities/{celebrity_id}/ideas/{idea_id} request received")
        idea = IdeaService.get_idea_in_celebrity(celebrity_id, idea_id)
        if idea:
            return idea.to_json(), 200
        return {'message': 'Idea not found'}, 404

class IdeaVote(Resource):
    @jwt_required()
    def post(self, celebrity_id, idea_id):
        print(f"POST /celebrities/{celebrity_id}/ideas/{idea_id}/vote request received")
        parser = reqparse.RequestParser()
        parser.add_argument('upvote', type=bool, required=True)
        args = parser.parse_args()
        print("Parsed args for voting:", args)

        user_id = get_jwt_identity()
        user = User.objects(id=user_id).first()

        if not user:
            return {'message': 'User not found'}, 404

        if args['upvote']:
            if idea_id in user.upvoted_ideas:
                return {'message': 'User has already upvoted this idea'}, 400
            user.upvoted_ideas.append(idea_id)
            if idea_id in user.downvoted_ideas:
                user.downvoted_ideas.remove(idea_id)
            user.save()
        else:
            if idea_id in user.downvoted_ideas:
                return {'message': 'User has already downvoted this idea'}, 400
            user.downvoted_ideas.append(idea_id)
            if idea_id in user.upvoted_ideas:
                user.upvoted_ideas.remove(idea_id)
            user.save()

        idea = IdeaService.update_votes(idea_id, celebrity_id, upvote=args['upvote'])
        if idea:
            return idea.to_json(), 200
        return {'message': 'Idea not found'}, 404

# class IdeaDelete(Resource):
#     def delete(self, celebrity_id, idea_title):
#         print(f"DELETE /celebrities/{celebrity_id}/ideas/{idea_title} request received")
#         success = IdeaService.delete_idea_by_id(celebrity_id, idea_title)
#         if success:
#             return {'message': f'Idea with title {idea_title} deleted.'}, 200
#         return {'message': 'Idea not found'}, 404

# class IdeaDeleteAll(Resource):
#     def delete(self, celebrity_id):
#         print(f"DELETE /celebrities/{celebrity_id}/ideas request received")
#         deleted_count = IdeaService.delete_all_ideas_from_celebrity(celebrity_id)
#         if deleted_count > 0:
#             return {'message': f'All {deleted_count} ideas deleted successfully.'}, 200
#         return {'message': 'Celebrity not found or no ideas to delete.'}, 404
