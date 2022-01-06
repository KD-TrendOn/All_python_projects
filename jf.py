import tkinter as tk

WIN_H=500
WIN_W=800
PANEL_H=WIN_H
PANEL_W=200
CANVAS_H=WIN_H
CANVAS_W=WIN_W-PANEL_W

win=tk.Tk()
win.title("График")
win.config(width=WIN_W, height=WIN_H)
win.resizable(False, False)

panel=tk.Frame(win, width=PANEL_W, height=PANEL_H, bd=4, relief=tk.GROOVE)
panel.place(x=0, y=0, width=PANEL_W, height=PANEL_H)

canvas=tk.Canvas(win, width=CANVAS_W, height=CANVAS_H, bg='#012')
canvas.place(x=PANEL_W, y=0, width=CANVAS_W, height=CANVAS_W)

def draw(x_left, x_right, y_bottom, y_top):
    dx= CANVAS_W/(x_right-x_left)
    dy=CANVAS_H/(y_top-y_bottom)

    cx=-x_left*dx
    cy= y_top*dy

    canvas.create_line(0, cy, CANVAS_W, cy, fill="white")
    canvas.create_line(cx, 0, CANVAS_H, cx, fill="white")

    x_step=(x_right-x_left)/12
    x=x_left
    while x <= x_right:
        x_canvas=(x-x_left)*dx
        canvas.create_line(x_canvas, cy-3, x_canvas, cy+3,fill="white")
        canvas.create_text(x_canvas, cy+12, text=str(round(x,1)),font="R",fill="white")

        x+=x_step
x_left, x_right= -5,15
y_bottom, y_top= -15,20
draw(x_left,x_right,y_bottom,y_top)

win.mainloop()