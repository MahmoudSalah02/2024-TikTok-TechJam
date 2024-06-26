from app.models.idea import Idea
from app.models.celebrity import Celebrity

class IdeaService:
    @staticmethod
    def add_idea_to_celebrity(celebrity_id, idea_data):
        print(f"Adding idea to celebrity with ID: {celebrity_id}")
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            new_idea = Idea(**idea_data)
            celebrity.ideas.append(new_idea)
            celebrity.save()
            print("Idea added to celebrity:", celebrity.to_json())
            return new_idea
        print("Celebrity not found.")
        return None

    @staticmethod
    def get_all_celebrity_ideas(celebrity_id):
        print(f"Fetching ideas for celebrity with ID: {celebrity_id}")
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            print(f"Found {len(celebrity.ideas)} ideas.")
            return celebrity.ideas
        print("Celebrity not found.")
        return []
    
    @staticmethod
    def get_idea_in_celebrity(celebrity_id, idea_id):
        print(f"Fetching idea '{idea_id}' for celebrity with ID: {celebrity_id}")
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            for idea in celebrity.ideas:
                if str(idea.id) == idea_id: # idea.id is of type UUID
                    print("Idea found:", idea.to_json())
                    return idea
            print(f"Idea '{idea_id}' not found in celebrity's ideas.")
        else:
            print("Celebrity not found.")
        return None

    @staticmethod
    def update_votes(celebrity_id, idea_id, upvote=True):
        print(f"Updating votes for idea '{idea_id}' in celebrity with ID: {celebrity_id}")
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            for idea in celebrity.ideas:
                if str(idea.id) == idea_id:
                    print("Current votes:", idea.votes)
                    idea.votes += 1 if upvote else -1
                    celebrity.save()
                    print("Updated votes:", idea.votes)
                    return idea
            print("Idea not found in celebrity's ideas.")
        else:
            print("Celebrity not found.")
        return None
