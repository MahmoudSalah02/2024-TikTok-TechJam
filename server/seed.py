from app import db, create_app
from app.models.idea import Idea
from app.models.celebrity import Celebrity
from flask import Flask
from mongoengine import connect

def create_seed_data():
    app = create_app()
    with app.app_context():
        # Ensure the database is clean
        Celebrity.drop_collection()

    # Create sample ideas
        celebrities_data = [
            {
                'name': 'IShowSpeed',
                'ideas': [
                    {'title': 'Ice bucket challenge', "description": "Stupidest shit I've heard", 'votes': 10},
                    {'title': 'Ronaldo gangbang', 'description': 'It is what it is', 'votes': 20}
                ]
            },
            {
                'name': 'John Cena',
                'ideas': [
                    {'title': 'Invisibility', 'description': 'Turns invisible', 'votes': 5},
                    {'title': 'Stronk', 'description': 'Smash Stuff', 'votes': 15}
                ]
            },
            {
                'name': 'Mahmoud Salah',
                'ideas': [
                    {'title': 'Fortnite Battle Pass', 'description': 'I just shit out my ass', 'votes': 7},
                    {'title': 'Fight Club', 'description': 'Fight everyone and hit them', 'votes': 12}
                ]
            }
    ]

    # Insert the data
    for celebrity_data in celebrities_data:
        celebrity = Celebrity(**celebrity_data)
        celebrity.save()
        print(f"Idea created with ID: {str(celebrity.id)}")


    print("Database seeded successfully.")


if __name__ == '__main__':
    create_seed_data()
