import pyautogui as pg
import keyboard as kb
import time
time.sleep(0)
pg.moveTo(608, 60, 0.5)
pg.rightClick(608, 60)
pg.moveTo(712, 422, 1)
pg.leftClick(712, 422)
pg.moveTo(1478, 12, 1)
pg.leftClick(1478, 12)
pg.moveTo(72, 879, 1)
pg.leftClick(72, 879)
kb.write("yandex")
kb.press_and_release("enter")
pg.moveTo(357, 427, 2)
pg.leftClick(357, 427)
time.sleep(0.5)
kb.write("тимур мем")
time.sleep(0.5)
kb.press_and_release("enter")
pg.moveTo(200, 155, 1.5)
pg.leftClick(200, 155)
pg.moveTo(972, 485, 2)
time.sleep(1)
pg.leftClick(972, 485)
time.sleep(1)
pg.alert("лох", "слитый", button="боже чел...")