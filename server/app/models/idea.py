from app import db

class Idea(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    votes = db.IntField(default=0)
    # comments = db.ListField(db.StringField())

    def to_json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "votes": self.votes,
            # "comments": self.comments
        }
