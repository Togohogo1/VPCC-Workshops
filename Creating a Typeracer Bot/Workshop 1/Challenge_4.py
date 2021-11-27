import time
from pynput.keyboard import Key, Controller

quote = ""
keyboard = Controller()

wpm = int(input("Input a WPM to type at: "))
cpm = wpm*5  # Characters per minute

# Time to select TypeRacer input box
time.sleep(2)

for i in quote:
    keyboard.press(i)
    keyboard.release(i)
    time.sleep(60/cpm)
