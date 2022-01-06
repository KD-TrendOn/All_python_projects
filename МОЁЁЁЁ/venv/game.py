from tkinter import *
from tkinter.colorchooser import askcolor
import random
import time


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(1, 1, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 2
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        print(pos[1])
        if pos[1] <= 0:
            self.y = random.randint(0, 5)
        if pos[3] >= self.canvas_height:
            self.y = -random.randint(0, 5)
        if pos[0] >= self.canvas_width:
            self.x = -random.randint(0, 5)
        if pos[2] <= 0:
            self.x = random.randint(0, 5)
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10,
        fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        pass


tk = Tk()
tk.title("Игра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=10)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, bg="blue")
canvas.pack()
tk.update()
colors = ["red", "blue", "orange",  "yellow", "lime"]
ball = Ball(canvas, "lime")
ball1 = Ball(canvas, "orange")
ball2 = Ball(canvas, "black")
ball3 = Ball(canvas, "red")
pad = Paddle(canvas, "violet")
while True:
    ball.draw()
    ball1.draw()
    ball2.draw()
    ball3.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


