import time
from pynput.keyboard import Key, Controller

# Time to open browser
time.sleep(1.5)

keyboard = Controller()
keyboard.press(Key.ctrl)
keyboard.press("t")
keyboard.release("t")
keyboard.release(Key.ctrl)
