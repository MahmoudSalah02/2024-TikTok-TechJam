from flask_restful import Resource, reqparse
from app.services.celebrity_service import CelebrityService

class CelebrityList(Resource):
    def get(self):
        print("GET /celebrities request received")
        celebrities = CelebrityService.get_all_celebrities()
        return [celebrity.to_json() for celebrity in celebrities], 200

    def post(self):
        print("POST /celebrities request received")
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        args = parser.parse_args()
        celebrity = CelebrityService.create_celebrity(args)
        return celebrity.to_json(), 201

class CelebrityDetail(Resource):
    def get(self, id):
        print(f"GET /celebrities/{id} request received")
        celebrity = CelebrityService.get_celebrity_by_id(id)
        if celebrity:
            return celebrity.to_json(), 200
        return {'message': 'Celebrity not found'}, 404

    def put(self, id):
        print(f"PUT /celebrities/{id} request received")
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=False)
        args = parser.parse_args()
        celebrity = CelebrityService.update_celebrity(id, args)
        if celebrity:
            return celebrity.to_json(), 200
        return {'message': 'Celebrity not found'}, 404
