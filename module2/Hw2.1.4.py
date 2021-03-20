import time
import math
from selenium import webdriver

url ="http://suninjuly.github.io/get_attribute.html"

try:
  browser = webdriver.Chrome()
  browser.get(url)
  treasure_variable = browser.find_element_by_id("treasure").get_attribute("valuex")
  textarea = browser.find_element_by_id("answer")
  robotCheckbox = browser.find_element_by_id("robotCheckbox")
  robotsRule = browser.find_element_by_id("robotsRule")
  button = browser.find_element_by_tag_name("button")
  def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
  y = calc(treasure_variable)
  textarea.send_keys(y)
  robotCheckbox.click()
  robotsRule.click()
  button.click()
  time.sleep(5)
finally:
  browser.quit()
