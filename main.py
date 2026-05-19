# ??

from turtle import Turtle, Screen  # from turtle <module> import Turtle <class>, Screen <class>

tim = Turtle()
tim.shape("turtle")
tim.color("#00ffff")
tim.color("cyan")


for i in range(4):
    tim.right(90)
    tim.forward(100)



screen = Screen()
screen.exitonclick()