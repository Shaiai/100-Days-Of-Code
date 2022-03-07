from itertools import count
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clock_wise():
    tim.left(10)

def counter_clock():
    tim.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=counter_clock)

screen.exitonclick()
