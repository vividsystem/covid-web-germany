#!/usr/bin/env python3
from . import db
from sqlalchemy.sql import func


class Entry(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  bundesland = db.Column(db.String(40))
  date = db.Column(db.DateTime(timezone=True), default=func.now()) # 1234-67-910
  cases = db.Column(db.Integer)
  new_cases = db.Column(db.Integer)
  cases_last_7days = db.Column(db.Integer)
  incidence_last_7days = db.Column(db.Integer)
  deaths = db.Column(db.Integer)

  #def __repr__(self):
  #  print(f"ID: {id}, date: {date}, cases:{cases}, new cases: {new_cases}, cases lasz 7 days: {cases_last_7days}, 7 day incidence: {incidence_last_7days}, deaths: {deaths}")
