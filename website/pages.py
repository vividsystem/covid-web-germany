#!/usr/bin/env python3
from flask import Blueprint, render_template, redirect
from .utilities import get_formatted_info
pages = Blueprint("pages", __name__)


@pages.route('/')
def normal():
  return redirect("/home")


@pages.route('/home')
def home():
  entries = get_formatted_info()
  return render_template("home.html", entries=entries)

@pages.route('/archive')
def archive():
  entries = get_formatted_info()
  return render_template("archive.html", entries=entries)