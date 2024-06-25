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
    def get_idea_in_celebrity(celebrity_id, idea_title):
        print(f"Fetching idea '{idea_title}' for celebrity with ID: {celebrity_id}")
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            for idea in celebrity.ideas:
                if idea.title == idea_title:
                    print("Idea found:", idea.to_json())
                    return idea
            print(f"Idea '{idea_title}' not found in celebrity's ideas.")
        else:
            print("Celebrity not found.")
        return None

    @staticmethod
    def update_celebrity_idea_votes(celebrity_id, idea_title, upvote=True):
        print(f"Updating votes for idea '{idea_title}' in celebrity with ID: {celebrity_id}")
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            for idea in celebrity.ideas:
                if idea.title == idea_title:
                    print("Current votes:", idea.votes)
                    idea.votes += 1 if upvote else -1
                    celebrity.save()
                    print("Updated votes:", idea.votes)
                    return idea
            print("Idea not found in celebrity's ideas.")
        else:
            print("Celebrity not found.")
        return None
    
    @staticmethod
    def delete_idea_by_id(celebrity_id, idea_title):
        print(f"Deleting idea '{idea_title}' from celebrity with ID: {celebrity_id}")
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            initial_count = len(celebrity.ideas)
            celebrity.ideas = [idea for idea in celebrity.ideas if idea.title != idea_title]
            if len(celebrity.ideas) < initial_count:
                celebrity.save()
                print(f"Idea '{idea_title}' deleted from celebrity with ID: {celebrity_id}.")
                return True
            else:
                print(f"Idea '{idea_title}' not found in celebrity's ideas.")
                return False
        print(f"Celebrity with ID {celebrity_id} not found.")
        return False

    @staticmethod
    def delete_all_ideas_from_celebrity(celebrity_id):
        print(f"Deleting all ideas from celebrity with ID: {celebrity_id}")
        celebrity = Celebrity.objects(id=celebrity_id).first()
        if celebrity:
            idea_count = len(celebrity.ideas)
            celebrity.ideas = []
            celebrity.save()
            print(f"All {idea_count} ideas deleted from celebrity with ID: {celebrity_id}.")
            return idea_count
        print(f"Celebrity with ID {celebrity_id} not found.")
        return 0

