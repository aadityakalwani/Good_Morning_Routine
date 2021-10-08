# ciao
# may the coding begin

# this file should open spotify and start playing lo-fi beats for me

# imports:
import time
import pyautogui


def open_spotify():

    pyautogui.hotkey("command", "shift", "s", interval=0.1)
    time.sleep(2)
    print("spotify is now open")


open_spotify()

print("completed")
