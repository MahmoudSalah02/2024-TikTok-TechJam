import mongoengine as db
import uuid

class Idea(db.EmbeddedDocument):
    id = db.UUIDField(required = True, default=uuid.uuid4)
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    votes = db.IntField(default=0)

    def to_json(self):
        return {
            "id": str(self.id),
            "title": self.title,
            "description": self.description,
            "votes": self.votes,
        }
