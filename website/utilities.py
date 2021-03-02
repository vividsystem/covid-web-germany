#!/usr/bin/env python3
from flask import jsonify
from .scraper import get_corona_info, update_db
from .models import Entry
from datetime import datetime
def make_json(entries):
  json = jsonify(cases = entries["cases"],
                new_cases = entries["new_cases"],
                cases_last7days = entries["cases_last7days"],
                incidence_last_7days = entries["incidence_last_7days"],
                deaths = entries["deaths"]
  )
  return json





def get_formatted_info():
  entries = {}
  entries_already_existing = False
  for i in Entry.query.all():
    if str(i.date).startswith(str(datetime.now())[0:10]):
      entries_already_existing = True
  if entries_already_existing == False:
    info = get_corona_info()
    update_db(info)
  for i in Entry.query.all():
    if str(i.date).startswith(str(datetime.now())[0:10]):
      entries[i.bundesland] = {"cases": i.cases,
                               "new_cases": i.new_cases,
                               "cases_last7days": i.cases_last_7days,
                               "incidence_last_7days": i.incidence_last_7days,
                               "deaths": i.deaths
                              }
  return entries