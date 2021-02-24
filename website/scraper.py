from selenium import webdriver
from os import getenv
from yaml import load, FullLoader
from sqlite3 import connect
from datetime import datetime
from time import strptime, strftime

website_path = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html"
def get_corona_info():
  config = load(open("./config.yaml"), Loader=FullLoader)
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  web_driver_path = config["webdriver_path"]
  driver = webdriver.Chrome(chrome_options=options)
  driver.get(website_path)


  elements = driver.find_elements_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[1]/table/tbody/tr")
  scrapped_info = list(map(lambda x: x.text, elements))
  scrapped_info = [x.replace('\xad', '').replace('\n','') for x in scrapped_info]
  dict_corona = {}
  for x in scrapped_info:
    formatted_info = x.replace(".", "").split(' ')
    dict_corona[formatted_info[0]] = formatted_info[1:6]
  
  return dict_corona


def update_db(info):
  from .models import Entry
  for i in info:
    print(i)




if __name__ == "__main__":
  info = get_corona_info()
  update_db(info)