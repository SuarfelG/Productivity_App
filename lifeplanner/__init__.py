from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "lifeplanner.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "1234567890"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


    from .models import authentication

    create_database(app)

    from .view import view
    from .auth import auth
    from .task import task

    app.register_blueprint(task, url_prefix="/")
    app.register_blueprint(view, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")



    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return authentication.query.get(int(id))

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print("Created database!")