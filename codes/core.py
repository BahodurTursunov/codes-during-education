from turtle import *
import turtle
from math import *

WIDTH, HEIGHT = 600, 600          # высота и ширина
windows = turtle.Screen()          # создали окно
windows.setup(WIDTH, HEIGHT)       # размер окна
#windows.screensize(3 * WIDTH, 3 * HEIGHT)
windows.bgcolor('blue')           # цвет задного фона
windows.delay(0)

windows.title("Снежинка Коха")

# turtle settings
snowflake = turtle.Turtle()
snowflake.pensize(3)                                 # размер ручки
snowflake.speed(1)                                   # скорость

snowflake.up()
snowflake.setpos(-WIDTH // 3, HEIGHT // 3)           # начальная координата
snowflake.down()
snowflake.color('gold')                              # цвет ручки

gens = int(numinput("Снежинка Коха", "Сколько итераций?", 3, minval=1, maxval=10))
# l-system settings
axiom = 'F++F++F'                   # "F" рисуем отрезок, "+" повернуть влево на 90 градусов
chr_1, rule_1 = 'F', 'F-F++F-F'     # "-" повернуть вправо на 90 градусов
step = 400
angle = 60

def apply_rules(axiom):
    res = ''
    for chr in axiom:
        if chr == chr_1:
            res += rule_1
        else:
            res += chr
    return res
print(apply_rules(axiom))
print("------------")



def get_result(gens, axiom):                # 0 axiom = F++F++F
    for gen in range(gens):                 # 1 axiom = F-F++F-F++F-F++F-F++F-F++F-F
        axiom = apply_rules(axiom)

    return axiom

print(get_result(gens, axiom))

for gen in range(gens):
    snowflake, up()
    turtle.goto(-WIDTH // 2 + 60, HEIGHT // 2 - 100)
    snowflake, down()

    turtle.clear()
    #turtle.write(f'Generation: {gen+1}', align="left", font=("Arial", 20, "normal"))


    snowflake.setheading(0)
    snowflake.goto(-WIDTH // 6, HEIGHT // 6)
    snowflake.clear()
    length = step / pow(3, gen)
    for chr in axiom:
        if chr == chr_1:
            snowflake.forward(length)
        elif chr == '+':
            snowflake.right(angle)
        elif chr == '-':
            snowflake.left(angle)
    axiom = apply_rules(axiom)

windows.exitonclick()