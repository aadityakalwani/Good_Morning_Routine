# ciao
# may the coding begin

# this file should open spotify and start playing lo-fi beats for me

# imports:
import time
import pyautogui


def open_spotify():

    # this part would open spotify itself using the raycast shortcut
    pyautogui.hotkey("command", "shift", "s", interval=0.1)
    time.sleep(3)
    print("spotify is now open")

    # this part would full screen
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("command")
    pyautogui.keyDown("f")
    time.sleep(0.5)
    pyautogui.keyUp("ctrl")
    pyautogui.keyUp("command")
    pyautogui.keyUp("f")

    time.sleep(3)


open_spotify()

print("completed")
