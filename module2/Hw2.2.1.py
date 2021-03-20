import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select


url ="http://suninjuly.github.io/selects1.html"

try:
  browser = webdriver.Chrome()
  browser.get(url)
  num1 = browser.find_element_by_id("num1").text
  num2 = browser.find_element_by_id("num2").text
  select  = Select(browser.find_element_by_id("dropdown"))
  select.select_by_value(str(int(num1)+int(num2)))
  button = browser.find_element_by_tag_name("button")
  button.click()
  time.sleep(5)
finally:
  browser.quit()