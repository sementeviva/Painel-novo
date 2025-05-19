from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'semente'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chatbot_db_evt1_user:9Uevdg6kJt27RUrupn72Ne0OXcAPsBib@dpg-d0l25bpr0fns7392c1ng-a/chatbot_db_evt1'

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from app.routes import bp
    app.register_blueprint(bp)

    return app
