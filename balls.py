from tkinter import *
from random import randint

WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self):
        self.R = randint(10, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10)
        self.color = "#" + ("%06x" % randint(0, 0xFFFFFF))
        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R,self.y + self.R, fill=self.color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:  
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    ball = Ball()
    balls.append(ball)


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
canvas.bind('<Button-1>', click_handler)
balls = []
# Делаем шаг перемещения и отрисовки шаров. Поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
tick()
root.mainloop()
