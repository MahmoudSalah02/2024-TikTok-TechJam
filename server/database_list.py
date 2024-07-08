from app import create_app, list_databases
from flask import Flask
from flask_mongoengine import MongoEngine
from dotenv import load_dotenv
import os


    
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        databases = list_databases()
        print("Database name: ", databases)