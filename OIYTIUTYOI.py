import keyboard
import pyautogui
import time
while True:
    keyboard.wait('y')
    for i in range(100):
        time.sleep(0.09)
        pyautogui.leftClick()