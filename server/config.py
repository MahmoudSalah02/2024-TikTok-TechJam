import os
from dotenv import load_dotenv

print("Loading environment variables from .env file...")
load_dotenv()  # Load environment variables from .env file

class Config:
    print("Configuring SECRET_KEY and MONGODB_SETTINGS...")
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    MONGODB_URI = os.environ.get('MONGODB_URI')
    if not MONGODB_URI:
        raise ValueError("No MONGODB_URI set for Flask application. Did you forget to set it in the .env file?")
    MONGODB_SETTINGS = {
        'host': MONGODB_URI
    }
    print("SECRET_KEY:", SECRET_KEY)
    print("MONGODB_URI:", MONGODB_URI)
    print("Configuration complete.")
