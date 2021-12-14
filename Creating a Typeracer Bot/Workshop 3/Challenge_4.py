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


N = int(input("Race now many races automatically: "))
tmp = N
avg = 0

while True:
    quit_captcha()

    if N == tmp:
        click_xpath(1, "//a[contains(@class, 'gwt-Anchor prompt-button bkgnd-green')]")
    else:
        click_xpath(1, "//a[contains(@class, 'raceAgainLink')]")

        # Getting WPM of race and adding to `avg`
        elem = driver.find_element(By.XPATH, "//div[contains(@class, 'rankPanelWpm rankPanelWpm-self')]")
        avg += int(elem.text[:-4])

    # Separating the removal of this popup from the captcha
    quit_account()

    if N == 0:
        break

    delay = float(input("Input your typing delay. To quit, input a number <= 0: "))

    if delay < 0:
        break

    text = find_text()
    send_text(text, delay)

    N -= 1

print(f"The average of those {tmp} race(s) is {avg//tmp} WPM")
