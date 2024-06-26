from app import db, create_app
from app.models.celebrity import Celebrity
from app.models.idea import Idea
import uuid

def create_celebrity(name, ideas_data):
    celebrity = Celebrity(name=name)
    for idea_data in ideas_data:
        new_idea = Idea(
            id=uuid.uuid4(),
            title=idea_data['title'],
            description=idea_data['description'],
            votes=idea_data['votes']
        )
        celebrity.ideas.append(new_idea)
    celebrity.save()
    return celebrity

def seed_database():
    # Sample data
    celebrities_data = [
        {
            'name': 'Celebrity 1',
            'ideas': [
                {'title': 'Revolutionize Social Media', 'description': 'A new platform that combines the best features of existing social media apps with enhanced privacy controls and no ads.', 'votes': 102},
                {'title': 'Eco-Friendly Packaging', 'description': 'Develop biodegradable and compostable packaging materials to replace plastic.', 'votes': 78}
            ]
        },
        {
            'name': 'Celebrity 2',
            'ideas': [
                {'title': 'Smart Home Automation', 'description': 'A system that integrates all home appliances and controls them via voice commands and mobile app.', 'votes': 150},
                {'title': 'Virtual Reality Fitness', 'description': 'A VR-based fitness program that offers immersive workouts, gamification, and social interaction.', 'votes': 120}
            ]
        },
        {
            'name': 'Celebrity 3',
            'ideas': [
                {'title': 'AI-Powered Personal Assistant', 'description': 'An AI assistant that helps manage your schedule, reminders, and daily tasks efficiently.', 'votes': 200},
                {'title': 'Blockchain Voting System', 'description': 'A secure, transparent, and tamper-proof voting system based on blockchain technology.', 'votes': 95}
            ]
        },
        {
            'name': 'Celebrity 4',
            'ideas': [
                {'title': 'Electric Vehicle Charging Network', 'description': 'An extensive network of fast-charging stations for electric vehicles across major cities.', 'votes': 130},
                {'title': 'Telehealth Platform', 'description': 'A comprehensive telehealth platform that offers remote consultations, prescriptions, and health monitoring.', 'votes': 145}
            ]
        },
        {
            'name': 'Celebrity 5',
            'ideas': [
                {'title': 'Renewable Energy Solutions', 'description': 'Innovative solutions to harness renewable energy sources like solar, wind, and tidal power.', 'votes': 180},
                {'title': 'Smart Agriculture', 'description': 'Using IoT and AI to optimize crop yields, monitor soil health, and reduce water usage in farming.', 'votes': 110}
            ]
        },
        {
            'name': 'Celebrity 6',
            'ideas': [
                {'title': 'Personalized Learning Platform', 'description': 'An AI-powered platform that offers personalized learning paths and resources for students of all ages.', 'votes': 160},
                {'title': 'Waste Management Solutions', 'description': 'Advanced waste management solutions that focus on recycling, composting, and reducing landfill waste.', 'votes': 125}
            ]
        },
        {
            'name': 'Celebrity 7',
            'ideas': [
                {'title': 'Urban Green Spaces', 'description': 'Creating more green spaces in urban areas to improve air quality, reduce heat, and provide recreational areas.', 'votes': 140},
                {'title': 'Mental Health Support App', 'description': 'An app that provides resources, counseling, and support for mental health issues.', 'votes': 175}
            ]
        },
        {
            'name': 'Celebrity 8',
            'ideas': [
                {'title': 'Autonomous Delivery Drones', 'description': 'Developing drones for automated delivery of goods, reducing traffic congestion and delivery times.', 'votes': 85},
                {'title': 'Electric Bike Sharing', 'description': 'A city-wide electric bike sharing system to reduce traffic congestion and promote eco-friendly transportation.', 'votes': 95}
            ]
        }
    ]

    # Clear the collections before seeding
    Celebrity.drop_collection()

    # Insert the data
    for celebrity_data in celebrities_data:
        create_celebrity(celebrity_data['name'], celebrity_data['ideas'])

    print("Database seeded successfully.")

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        seed_database()