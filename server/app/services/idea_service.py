from app.models.idea import Idea

class IdeaService:
    @staticmethod
    def create_idea(data):
        print("Creating a new idea with data:", data)
        idea = Idea(**data)
        idea.save()
        print("Idea created with ID:", str(idea.id))
        return idea

    @staticmethod
    def get_all_ideas():
        print("Fetching all ideas sorted by votes...")
        ideas = Idea.objects().order_by('-votes')
        print(f"Found {len(ideas)} ideas.")
        return ideas

    @staticmethod
    def get_idea_by_id(idea_id):
        print("Fetching idea with ID:", idea_id)
        idea = Idea.objects(id=idea_id).first()
        if idea:
            print("Idea found:", idea.to_json())
        else:
            print("Idea not found.")
        return idea

    @staticmethod
    def update_votes(idea_id, upvote):
        print("Updating votes for idea with ID:", idea_id)
        idea = Idea.objects(id=idea_id).first()
        if not idea:
            return None
        
        print("Current votes:", idea.votes)
        if upvote:
            idea.votes += 1
        else:
            idea.votes -= 1

        idea.save()
        print("Updated votes:", idea.votes)
        
        return idea
    
    @staticmethod
    def delete_idea_by_id(idea_id):
        print("Deleting idea with ID:", idea_id)
        idea = Idea.objects(id=idea_id).first()
        if idea:
            idea.delete()
            print(f"Idea with ID {idea_id} deleted.")
            return True
        print(f"Idea with ID {idea_id} not found.")
        return False

    @staticmethod
    def delete_all_ideas():
        print("Deleting all ideas...")
        result = Idea.objects.delete()
        print(f"All ideas deleted. {result.deleted_count} documents were removed.")
        return result.deleted_count

