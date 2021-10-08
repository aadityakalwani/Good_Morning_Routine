# ciao
# may the coding begin

# this file should open spotify and start playing lo-fi beats for me

# imports:
import time
import pyautogui

# open spotify


def open_spotify():
    print("opening spotify")
    pyautogui.keyDown("command")
    pyautogui.keyDown("space")
    time.sleep(1)
    pyautogui.write("spotify")
    pyautogui.press("enter")

