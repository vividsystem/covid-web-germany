from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME = "corona.db"

def create_app():
  app = Flask(__name__)
  app.config["SECRET_KEY"] = "sgdfgsgsdg"
  app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///../db/{DB_NAME}"
  db.init_app(app)
  from .pages import pages
  app.register_blueprint(pages, url_prefix="/")

  from .models import Entry

  create_db(app)

  return app

def create_db(app):
  if not path.exists("db/"+ DB_NAME):
    db.create_all(app=app)
    print('Created database!')