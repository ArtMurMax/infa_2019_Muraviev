from tkinter import *
from random import randrange as rnd, choice
import math
import time

root = Tk()
root.geometry('800x600')

canv = Canvas(root, width=200, height=200, bg='white')
canv.pack(fill=BOTH, expand=1)
lab = Label(canv, bg='black', fg='white', width=20)
lab['text'] = '0'

Colors = ['red', 'orange', 'yellow', 'green', 'blue']


class Ball:
    def __init__(self, cord=None, vel=None, size=None, color=None):
        self.cord = [rnd(100, 700), rnd(100, 500)] if cord is None else cord
        self.vel = [rnd(10, 50) * choice([-1, 1]), rnd(10, 50) * choice([-1, 1])] if vel is None else vel
        self.size = rnd(30, 50) if size is None else size
        self.color = choice(Colors) if color is None else color
        self.object = canv.create_oval(self.cord[0] - self.size, self.cord[1] - self.size, self.cord[0] + self.size, self.cord[1] + self.size, fill = self.color, width=0)

#canv.addtag_withtag("ball", self.object)

    def move(self, dt=0.1):
        if self.cord[0] + self.vel[0] * dt - self.size < 0 or self.cord[0] + self.vel[0] + self.size * dt > 800:
            self.vel[0] *= -1
        if self.cord[1] + self.vel[1] * dt - self.size < 0 or self.cord[1] + self.vel[1] * dt + self.size > 600:
            self.vel[1] *= -1
        self.cord = [self.cord[0] + self.vel[0] * dt, self.cord[1] + self.vel[1] * dt]
        canv.move(self.object, self.vel[0] * dt, self.vel[1] * dt)


    def delete(self):
        canv.delete(self.object)


    def is_caught(self, x, y):
        return ((x - self.cord[0]) ** 2 + (y - self.cord[1]) ** 2 < self.size ** 2)


def update_scene():
    for ball in balls:
        ball.move()
    root.after(10, update_scene)


def mouse_click(event):
    for ball in balls:
        if ball.is_caught(event.x, event.y):
            ball.delete()
            lab['text'] = str(int(lab['text']) + 1)

balls = [Ball() for i in range(15)]
update_scene()

canv.bind('<Button-1>', mouse_click)
lab.pack()
#root.bind('<Key-1>', lambda event: print(event))

root.mainloop()