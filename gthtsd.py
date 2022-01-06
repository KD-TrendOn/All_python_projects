import turtle
import math
from turtle import *
a = Turtle()
a.hide()
def prtr(k, b, c):
    a.fd(k)
    a.bk(k)
    a.left(90)
    a.fd(b)
    a.right(90)
    a.radians()
    a.right(math.pi / 2 - math.asin(k/c))
    a.fd(c)
prtr(int(input('Катет')), int(input('Катет')), int(input('Гипотенуза')))
turtle.mainloop()
