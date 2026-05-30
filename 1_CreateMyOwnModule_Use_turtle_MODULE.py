import another_module

print(another_module.another_variable)


from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)

# Before we print our screen out, we need finish all outsettings about the turtle
timmy.shape("turtle")
timmy.color("cyan")

print(timmy.position())
timmy.forward(100)
print(timmy.position())


my_screen = Screen() # a window pops up for an instant. THIS line of code CREATES the window.
# print(my_screen.canvheight)
my_screen.exitonclick()
