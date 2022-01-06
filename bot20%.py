import pyautogui
import time
time.sleep(2)
while True:
    while True:
        pyautogui.write('20')
        pyautogui.press('enter')
        time.sleep(0.5)
        a = pyautogui.position()
        if a[0] > 1000 and a[1] < 200:
            break
    pyautogui.moveTo(635, 70, 1)
    pyautogui.rightClick()
    pyautogui.moveTo(725, 451)
    pyautogui.leftClick()
    pyautogui.moveTo(280, 616)
    pyautogui.leftClick()