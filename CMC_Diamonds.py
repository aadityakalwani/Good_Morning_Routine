# ciao
# may the coding begin

# references:
# >>> import pyautogui
#
# >>> screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
#
# >>> currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
#
# >>> pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
#
# >>> pyautogui.click()          # Click the mouse.
# >>> pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
# >>> pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
#
# >>> pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
# >>> pyautogui.doubleClick()    # Double click the mouse.
# >>> pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
# Use tweening/easing function to move mouse over 2 seconds.
#
# >>> pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
# >>> pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
#
# >>> pyautogui.keyDown('shift') # Press the Shift key down and hold it.
# >>> pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
# >>> pyautogui.keyUp('shift')   # Let go of the Shift key.
#
# >>> pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
#
# >>> pyautogui.alert('This is the message to display.')
# Make an alert box appear and pause the program until OK is clicked.

import time
import pyautogui


def collect_diamonds():

    # this part opens coinmarketcap
    time.sleep(0.5)
    pyautogui.keyDown("command")
    pyautogui.press("space")
    pyautogui.keyUp("command")
    pyautogui.write("cmc", interval=0.5)
    pyautogui.press("enter")

    # this part would open full screen
    time.sleep(0.5)
    pyautogui.hotkey("cmd, ctrl, f")

    # this part clicks on the diamonds button
    time.sleep(1)
    pyautogui.moveTo(1308, 116)
    time.sleep(0.5)
    pyautogui.click()

    # this part clicks on the "collect diamonds" button
    time.sleep(0.5)
    pyautogui.moveTo(1500, 680)
    time.sleep(0.5)
    pyautogui.click()

    # this part closes the popup window
    pyautogui.moveTo(800, 700)
    time.sleep(0.5)
    pyautogui.click()

    print("cool, done")


collect_diamonds()

# had a random cool idea, will eventually use b3ar's google home type jarvis thingy to have a morning routine which will have this as part of it
