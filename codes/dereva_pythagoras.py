from turtle import *
import turtle
from math import *

windows = turtle.Screen()
windows.setup(700, 700)
windows.bgcolor("white")


wheel = 12
pensize(2)
colormode(255)
pencolor("black")


def avance(l, n):
    if n == 0:
        forward(l)
    else:
        right(135)                  # на правую сторону 135 градусов
        forward(l * sqrt(2) / 2)    # длина 70,71
        left(90)                    # на левую сторону 90 градусов
        avance(l * sqrt(2) / 2, n - 1)  #avance(70.71, n-1)
        left(90)                    # на левую сторону 90 градусов
        forward(l * sqrt(2) / 2)    # длина 70,71
        left(90)                    # на левую сторону 90 градусов
        forward(l * sqrt(2) / 2)    # длина 70,71
        right(135)                  # на правую сторону 135 градусов

        forward(l)                  # длина 100

        right(135)
        forward(l * sqrt(2) / 2)
        left(90)
        forward(l * sqrt(2) / 2)
        left(90)
        avance(l * sqrt(2) / 2, n - 1)
        left(90)
        forward(l * sqrt(2) / 2)
        right(135)
        turtle.speed("fast")
def carre(l, n):
    forward(l)
    left(90)
    forward(l)
    left(90)
    avance(l, n)
    left(90)
    forward(l)
    mainloop()

#Principal Program

windows.title("Дерево Пифагора")
e = numinput("Дерево Пифагора", "Сколько этапов ?", 1, minval=0, maxval=100)
x = 100
speed(10)
hideturtle()
carre(x, e)
