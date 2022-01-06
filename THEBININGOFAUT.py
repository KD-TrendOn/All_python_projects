import pyautogui as pg
import keyboard
import time
time.sleep(2)
for i in range(0, 400):
    time.sleep(.3)
    pg.write('achievement ' + str(i))
    time.sleep(.3)
    keyboard.press('enter')
    time.sleep(.3)
    keyboard.release('enter')
