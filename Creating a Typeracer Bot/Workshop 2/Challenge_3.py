import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://typeracer.com/")

input("Hit enter after clicking \"Enter a Typing Race\": ")

words = []
elem = driver.find_elements_by_xpath("//span[@unselectable='on']")

for i in elem:
    words.append(i.text)

tr_text = "".join(words[:-1]) + f" {words[-1]}"

input("Hit enter to when the input box is active: ")
input_box = driver.find_element_by_class_name("txtInput")

for i in tr_text:
    input_box.send_keys(i)
    time.sleep(0.05)
