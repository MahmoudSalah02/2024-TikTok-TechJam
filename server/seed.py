from app import create_app
from app.models.idea import Idea
import os

def create_seed_data():
    app = create_app()
    with app.app_context():
        # Ensure the database is clean
        Idea.objects.delete()

        # Define seed data
        ideas = [
            {
                "title": "Build a chatbot",
                "description": "Create an AI-powered chatbot for customer service",
                "votes": 10
            },
            {
                "title": "Develop a mobile app",
                "description": "Develop a cross-platform mobile app for project management",
                "votes": 5
            },
            {
                "title": "Launch a marketing campaign",
                "description": "Launch a social media marketing campaign to increase brand awareness",
                "votes": 8
            },
            {
                "title": "Create an online course",
                "description": "Develop an online course to teach programming skills",
                "votes": 12
            },
            {
                "title": "Organize a hackathon",
                "description": "Organize a community hackathon event to foster innovation",
                "votes": 7
            }
        ]

        # Insert seed data
        for idea_data in ideas:
            idea = Idea(**idea_data)
            idea.save()
            print(f"Idea created with ID: {str(idea.id)}")

if __name__ == '__main__':
    create_seed_data()
