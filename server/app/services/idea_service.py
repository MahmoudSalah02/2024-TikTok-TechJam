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
    def update_votes(idea_id, upvote=True):
        print("Updating votes for idea with ID:", idea_id)
        idea = Idea.objects(id=idea_id).first()
        if idea:
            print("Current votes:", idea.votes)
            idea.votes += 1 if upvote else -1
            idea.save()
            print("Updated votes:", idea.votes)
            return idea
        print("Idea not found.")
        return None
