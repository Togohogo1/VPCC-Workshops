import time

from bs4 import BeautifulSoup
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
        # Get the HTML of the current page
        src = driver.page_source
        soup = BeautifulSoup(src, "html.parser")
        span = soup.findAll("span")

        text = ""

        for i in span:
            if "unselectable" in str(i):
                text += i.text

        if text:
            break

    # Text to be typed
    return text


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


def click_xpath(timeout, *xpaths):
    try:
        wait = WebDriverWait(driver, timeout)

        for xpath in xpaths:
            elem = wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
    except TimeoutException:
        pass


def quit_captcha():
    click_xpath(1,
        "//button[contains(@class, 'gwt-Button')]",
        "//button[contains(@class, 'gwt-Button')]",
        "//div[contains(@title, 'close this popup')]"
    )


def quit_account():
    click_xpath(1, "//div[contains(@title, 'close this popup')]")


first_race = True

while True:
    quit_captcha()

    if first_race:
        delay = float(input("Input your typing delay. To quit, input a number <= 0: "))
        mode = int(input("Input 0 for race mode, 1 for practice mode: "))

        if mode == 0:
            click_xpath(1, "//a[contains(@class, 'gwt-Anchor prompt-button bkgnd-green')]")
        else:
            click_xpath(1, "//a[contains(@class, 'gwt-Anchor prompt-button bkgnd-blue')]")

        first_race = False
    else:
        op = int(input("Enter 0 to continue, 1 to return to the main menu: "))

        if op:
            driver.get("https://typeracer.com/")
            first_race = True
            continue
        else:
            click_xpath(1, "//a[contains(@class, 'raceAgainLink')]")

            #  Separating the removal of this popup from the captcha
            quit_account()

            delay = float(input("Input your typing delay. To quit, input a number <= 0: "))

    if delay <= 0:
        break

    text = find_text()
    send_text(text, delay)
