from flask_restful import Resource, reqparse
from app.services.celebrity_service import CelebrityService
from flask import send_file, request, jsonify
import io

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

class CelebrityPicture(Resource):
    def get(self, id):
        print(f"GET /celebrities/{id}/picture request received")
        celebrity = CelebrityService.get_celebrity_by_id(id)
        if not celebrity:
            return {'message': 'Celebrity not found'}, 404
        image_data = CelebrityService.get_profile_picture(celebrity.profile_picture)
        if not image_data:
            return {'message': 'Profile picture not found'}, 404
        return send_file(
        io.BytesIO(image_data),
        mimetype='image/jpeg',
        as_attachment=True,
        download_name=f"{id}_profile_picture.jpg"
        )


    def post(self, id):
        print(f"POST /celebrities/{id}/picture request received")
        if 'profile_picture' not in request.files:
            return jsonify({'message': 'No file part'}), 400

        file = request.files['profile_picture']
        if file.filename == '':
            return jsonify({'message': 'No selected file'}), 400

        celebrity = CelebrityService.save_profile_picture(id, file.read())
        if isinstance(celebrity, dict) and 'message' in celebrity:
            return celebrity, 404

        return celebrity.to_json(), 200