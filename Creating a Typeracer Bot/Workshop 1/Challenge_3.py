import time
from pynput.keyboard import Key, Controller

quote = "bruh sus"  # Copy and paste from inspect element
keyboard = Controller()

for i in quote:
    keyboard.press(i)
    keyboard.release(i)
    time.sleep(0.05)
