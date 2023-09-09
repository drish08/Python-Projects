# importing the library
from turtle import *


# Function for position
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()


# to draw the left eye
def leftEye(x, y):
    my_goto(x, y)
    seth(0)
    fillcolor('#333333')
    begin_fill()
    circle(22)
    end_fill()

    my_goto(x, y + 10)
    fillcolor('#000000')
    begin_fill()
    circle(10)
    end_fill()

    my_goto(x + 6, y + 22)
    fillcolor('#ffffff')
    begin_fill()
    circle(10)
    end_fill()


# To draw the right eye
def rightEye(x, y):
    my_goto(x, y)
    seth(0)
    fillcolor('#333333')
    begin_fill()
    circle(22)
    end_fill()

    my_goto(x, y + 10)
    fillcolor('#000000')
    begin_fill()
    circle(10)
    end_fill()

    my_goto(x - 6, y + 22)
    fillcolor('#ffffff')
    begin_fill()
    circle(10)
    end_fill()
