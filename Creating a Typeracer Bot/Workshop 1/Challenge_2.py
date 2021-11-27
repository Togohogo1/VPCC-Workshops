import time
from pynput.keyboard import Key, Controller


def open_tab():
    keyboard.press(Key.ctrl)
    keyboard.press("t")
    keyboard.release("t")
    keyboard.release(Key.ctrl)


def search(word):
    open_tab()

    for i in word:
        keyboard.press(i)
        keyboard.release(i)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


# Time to open browser
time.sleep(1.5)

keyboard = Controller()

for i in ["dog", "cat", "mouse"]:
    time.sleep(1.5)
    search(i)
