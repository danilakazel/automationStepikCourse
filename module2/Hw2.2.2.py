import time
import math
from selenium import webdriver


url ="http://suninjuly.github.io/execute_script.html"

try:
  browser = webdriver.Chrome()
  browser.get(url)
  x = browser.find_element_by_id("input_value").text
  def calc(x):
      return str(math.log(abs(12 * math.sin(int(x)))))
  y = calc(x)
  button = browser.find_element_by_tag_name("button")
  button = browser.find_element_by_tag_name("button")
  textarea = browser.find_element_by_id("answer")
  textarea.send_keys(y)
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  robotCheckbox = browser.find_element_by_id("robotCheckbox")
  robotCheckbox.click()
  robotsRule = browser.find_element_by_id("robotsRule")
  robotsRule.click()
  button.click()
  time.sleep(5)
finally:
  browser.quit()