from flask import Blueprint, render_template, redirect
pages = Blueprint("pages", __name__)


@pages.route('/')
def normal():
  return redirect("/home")


@pages.route('/home')
def home():
  return render_template("home.html")

@pages.route('/archive')
def archive():
  return render_template("archive.html")