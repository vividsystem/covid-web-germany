from . import db
from sqlalchemy.sql import func


class Entry(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.DateTime(timezone=True), default=func.now()) # 1234-67-910
  cases = db.Column(db.Integer)
  new_cases = db.Column(db.Integer)
  cases_last_7days = db.Column(db.Integer)
  incidence_last_7days = db.Column(db.Integer)
  deaths = db.Column(db.Integer)