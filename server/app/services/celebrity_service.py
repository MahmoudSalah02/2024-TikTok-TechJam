from app.models.celebrity import Celebrity
from app.models.idea import Idea

class CelebrityService:
    @staticmethod
    def create_celebrity(data):
        print("Creating a new celebrity with data:", data)
        celebrity = Celebrity(**data)
        celebrity.save()
        print("Celebrity created with ID:", str(celebrity.id))
        return celebrity

    @staticmethod
    def get_all_celebrities():
        print("Fetching all celebrities...")
        celebrities = Celebrity.objects()
        print(f"Found {len(celebrities)} celebrities.")
        return celebrities

    @staticmethod
    def get_celebrity_by_id(celebrity_id):
        print("Fetching celebrity with ID:", celebrity_id)
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            print("Celebrity found:", celebrity.to_json())
        else:
            print("Celebrity not found.")
        return celebrity

    @staticmethod
    def update_celebrity(celebrity_id, data):
        print("Updating celebrity with ID:", celebrity_id)
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            celebrity.update(**data)
            celebrity.reload()
            print("Celebrity updated:", celebrity.to_json())
            return celebrity
        print("Celebrity not found.")
        return None
