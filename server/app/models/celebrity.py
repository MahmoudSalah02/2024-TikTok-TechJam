import mongoengine as db
from app.models.idea import Idea

class Celebrity(db.Document):
    name = db.StringField(required=True)
    ideas = db.ListField(db.EmbeddedDocumentField(Idea))

    def to_json(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "ideas": [idea.to_json() for idea in self.ideas]
        }