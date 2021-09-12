# ciao
# may the coding begin

import webbrowser
import time
import pyautogui


def open_crypto():
    pyautogui.keyDown("command")
    pyautogui.keyDown("space")
    time.sleep(0.1)
    pyautogui.keyUp("space")
    pyautogui.keyUp("command")
    time.sleep(0.1)
    pyautogui.write("chrome")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.25)
    pyautogui.keyDown("command")
    pyautogui.keyDown("n")
    time.sleep(0.1)
    pyautogui.keyUp("n")
    pyautogui.keyUp("command")
    time.sleep(0.1)

    webbrowser.open_new("https://alpha.multifarm.fi/assets")
    time.sleep(0.1)
    webbrowser.open_new("https://dailydefi.org/tools/impermanent-loss-calculator/")
    time.sleep(0.1)
    webbrowser.open_new("https://pancakeswap.finance/")
    time.sleep(0.1)
    webbrowser.open_new("https://apeswap.finance/")
    time.sleep(0.1)
    webbrowser.open_new("https://www.buffaloswap.org/")
    time.sleep(0.1)
    webbrowser.open_new("https://bear.honeyfarm.finance/")
    time.sleep(0.1)
    webbrowser.open_new("https://cobra.exchange/#/staking/pools")
    time.sleep(0.1)
    webbrowser.open_new("https://babyswap.finance/")
    time.sleep(0.1)
    webbrowser.open_new("https://kavian.finance/")
    time.sleep(0.1)
    webbrowser.open_new("https://vfat.tools/bsc/")

    print("done")


open_crypto()
