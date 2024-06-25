import mongoengine as db

class Idea(db.EmbeddedDocument):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    votes = db.IntField(default=0)
    # comments = db.ListField(db.StringField())

    def to_json(self):
        return {
            "title": self.title,
            "description": self.description,
            "votes": self.votes,
            # "comments": self.comments
        }
