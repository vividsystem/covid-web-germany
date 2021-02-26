#!/usr/bin/env python3
from flask import Blueprint, render_template, redirect
from .models import Entry
from datetime import datetime
from .scraper import get_corona_info, update_db
pages = Blueprint("pages", __name__)


@pages.route('/')
def normal():
  return redirect("/home")


@pages.route('/home')
def home():
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
  return render_template("home.html", entries=entries)

@pages.route('/archive')
def archive():
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
      entries[i.bundesland] = {"date": str(i.date)[0:10],
                               "cases": i.cases,
                               "new_cases": i.new_cases,
                               "cases_last7days": i.cases_last_7days,
                               "incidence_last_7days": i.incidence_last_7days,
                               "deaths": i.deaths
                              }
  return render_template("archive.html", entries=entries)