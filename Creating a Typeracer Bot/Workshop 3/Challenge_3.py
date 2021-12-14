import time

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Suppress error/warning/log messages in command prompt
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=options)
driver.get("https://typeracer.com/")


def find_text():
    while True:
        words = []
        elem = driver.find_elements(By.XPATH, "//span[@unselectable='on']")

        for i in elem:
            words.append(i.text)

        if words:
            break

    # Text to be typed
    return "".join(words[:-1]) + f" {words[-1]}"

def send_text(text, delay):
    try:
        # Click the input box when it can be clicked (allow it 15 seconds)
        wait = WebDriverWait(driver, 15)
        elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "txtInput")))
    except TimeoutException:
        pass
    else:
        for i in text:
            elem.send_keys(i)
            time.sleep(delay)


def quit_captcha():
    try:
        wait = WebDriverWait(driver, 1)
        begin_test = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'gwt-Button')]"))).click()
        submit = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'gwt-Button')]"))).click()
        x = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@title, 'close this popup')]"))).click()
    except TimeoutException:
        pass


def quit_account():
    try:
        wait = WebDriverWait(driver, 1)
        x = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'xButton')]"))).click()
    except TimeoutException:
        pass


while True:
    quit_captcha()
    delay = float(input("Input your typing delay after entering a race. To quit, input a number <= 0: "))

    # Separating the removal of this popup from the captcha
    quit_account()

    if delay <= 0:
        break

    text = find_text()
    send_text(text, delay)
