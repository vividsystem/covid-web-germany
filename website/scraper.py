#!/usr/bin/env python3
from selenium import webdriver
from os import getenv
from . import db, config

def get_corona_info():
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  web_driver_path = config["webdriver_path"]
  website_path = config["website_path"]
  driver = webdriver.Chrome(chrome_options=options)
  driver.get(website_path)


  elements = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[1]/table/tbody/tr")
  scrapped_info = list(map(lambda x: x.text, elements))
  scrapped_info = [x.replace('\xad', '').replace('\n','').replace('ü', 'ue').replace('ä', 'ae') for x in scrapped_info]
  dict_corona = {}
  for x in scrapped_info:
    formatted_info = x.replace(".", "").split(' ')
    dict_corona[formatted_info[0]] = formatted_info[1:6]
  
  return dict_corona


def update_db(info):
  from .models import Entry
  for i in info:
    
    newEntry = Entry(bundesland=str(i), cases=int(info[i][0]), new_cases=int(info[i][1]), cases_last_7days=int(info[i][2]), incidence_last_7days=int(info[i][3]), deaths=int(info[i][4]))
    db.session.add(newEntry)
    db.session.commit()