import turtle as my_turtle
from turtle import speed,reset,goto

speed(10)
reset()

def drawoval(rad):
    for x in range(2):
        my_turtle.circle(rad,90)
        my_turtle.circle(rad//2,90)

drawoval(50)
drawoval(-10)
goto(-32,25)
drawoval(-10)
goto(45,65)
drawoval(20)
goto(10,73)
drawoval(10)
goto(55,45)
drawoval(10)
goto(-15,3)
my_turtle.left(-135)
my_turtle.forward(20)


my_turtle.done()