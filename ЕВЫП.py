import pyautogui
import time

a = True
time.sleep(5)
while a:
    pyautogui.keyDown('space')
    time.sleep(0.1)
    pyautogui.keyUp('space')
    time.sleep(0.3)
