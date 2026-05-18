# Use functions as parameter - High order functions
# event listeners - 1. a High order function that takes func as inputs 2. also requires a key input

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()
