import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('C:\\Users\\Administrator\\Desktop\\CS 065\\chromedriver.exe')
driver.get('http://www.drake.edu/')
page=driver.page_source
import urllib.request
from bs4 import BeautifulSoup
print(type(page))
soup = BeautifulSoup(page, "html.parser")
table = soup.find("form",{'id':"mobileSearchForm"})
print(table)

