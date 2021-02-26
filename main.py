#!/usr/bin/env python3
from flask import Flask, render_template, redirect
from website import create_app
from website.models import Entry
from website.scraper import get_corona_info, update_db
from datetime import datetime

if __name__ == "__main__":
  app = create_app()
  app.run(host="0.0.0.0", debug=False)