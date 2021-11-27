import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://typeracer.com/")

input("Hit enter to when the input box is active: ")

elem = driver.find_element_by_class_name("txtInput")
print(type(elem), elem)
elem.send_keys("txtInput")
