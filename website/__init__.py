#!/usr/bin/env python3

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from yaml import load, FullLoader

db = SQLAlchemy()
config = load(open("./config.yaml"), Loader=FullLoader)
DB_NAME = "corona.db"

def create_app():
  app = Flask(__name__)
  app.config["SECRET_KEY"] = "sgdfgsgsdg"
  app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///../db/{DB_NAME}"
  db.init_app(app)
  app.app_context().push()

  from .pages import pages
  app.register_blueprint(pages, url_prefix="/")

  from .api import api
  app.register_blueprint(api, url_prefix="/api/")

  from .models import Entry
  create_db(app)

  return app

def create_db(app):
  if not path.exists("db/"+ DB_NAME):
    db.create_all(app=app)
    print('Created database!')

if __name__ == "__main__":
  app = create_app()
  create_db(app)