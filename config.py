import os

class Config:
    SECRET_KEY = 'semente'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://semente:semente@localhost:5432/painel_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False