import turtle
a = turtle.Turtle()
a.speed(0)
def sq(b):
    a.penup()
    a.forward(b)
    a.left(90)
    a.pendown()
    a.forward(b)
    a.left(90)
    a.forward(b)
    a.left(90)
    a.penup()
    a.forward(b)
    a.left(90)
    a.pendown()
for i in range(1, 11):
    bob = 1.41421 ** i
    for i in range(72):
        sq(round(10 * bob))
        a.right(5)
turtle.done()