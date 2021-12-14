import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Suppress error/warning/log messages in command prompt
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get("https://typeracer.com/")

while True:
    op = input("Input q to quit. Input anything else after entering a race: ")

    if op == "q":
        break

    while True:
        words = []
        elem = driver.find_elements(By.XPATH, "//span[@unselectable='on']")

        for i in elem:
            words.append(i.text)

        if words:
            break

    # Text to be typed
    tr_text = "".join(words[:-1]) + f" {words[-1]}"

    input("Hit enter to when the input box is active: ")
    input_box = driver.find_element(By.CLASS_NAME, "txtInput")

    for i in tr_text:
        input_box.send_keys(i)
        time.sleep(0.1)
