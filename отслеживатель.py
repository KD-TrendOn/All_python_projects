import pyautogui as pg
import time
pipi = []
x = 0
a = int(input())
while x < a:
    pipi.append(pg.position())
    time.sleep(0.1)
    x += 0.1

time.sleep(3)
for x in pipi:
    pg.moveTo(x, duration= 0.1)
