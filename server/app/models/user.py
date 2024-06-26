from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password_hash = db.StringField(required=True)
    upvoted_ideas = db.ListField()
    downvoted_ideas = db.ListField()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "upvoted_ideas": self.upvoted_ideas,
            "downvoted_ideas": self.downvoted_ideas
        }
