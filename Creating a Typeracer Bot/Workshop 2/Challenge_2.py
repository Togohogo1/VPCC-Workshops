import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://typeracer.com/")

input("Hit enter after clicking \"Enter a Typing Race\": ")

words = []
elem = driver.find_elements_by_xpath("//span[@unselectable='on']")

for i in elem:
    words.append(i.text)

print("".join(words[:-1]) + f" {words[-1]}")
