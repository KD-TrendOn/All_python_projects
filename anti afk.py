import pyautogui
import time
while True:
    time.sleep(2)
    a = pyautogui.position()
    if a[0] > 600 and a[1] < 350:
        quit()
    else:
        pyautogui.moveTo(300, 700, 2)
        time.sleep(2)
        pyautogui.moveTo(300, 350, 2)
