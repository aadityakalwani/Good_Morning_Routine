# ciao
# may the coding begin

# this file should open spotify and start playing lo-fi beats for me

# imports:
import time
import pyautogui


def open_spotify():

    # this part would open spotify itself using the raycast shortcut
    pyautogui.hotkey("command", "shift", "s", interval=0.1)
    time.sleep(5)
    print("spotify is now open")

    # this part would full screen
    pyautogui.hotkey("control", "command", "f", interval=0.1)
    time.sleep(3)


open_spotify()

print("completed")
