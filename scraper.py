from selenium import webdriver
from os import getenv
from yaml import load, FullLoader
import time
website_path = "https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html"

config = load(open("./config.yaml"), Loader=FullLoader)
options = webdriver.Options()
options.add_argument('--headless')
web_driver_path = config["webdriver_path"]
driver = webdriver.Chrome(options=options)
driver.get(website_path)
element = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[1]/table/tbody/tr[9]/td[2]")
time.sleep(10)
driver.quit()
print(element.text())