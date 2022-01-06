import keyboard as kb
import time

time.sleep(3)
x = 0
faf = ["андрей бот"]
while x <= 10:
    for d in faf:
        kb.write(d)
        time.sleep(0.4)
        kb.press_and_release("enter")
        time.sleep(1)
    x += 1