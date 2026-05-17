from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_list = []

for i in range(6):
    # turtle_list[i] = Turtle(shape="Turtle")  # IndexError: list assignment index out of range
    new_turtle = Turtle(shape="turtle")
    turtle_list.append(new_turtle)
    turtle_list[i].color(colors[i])   # turtle_list[i].color = colors[i] incorrect!
    turtle_list[i].penup()
    turtle_list[i].goto(x=-230, y = -125 + i*50)

screen.exitonclick()

