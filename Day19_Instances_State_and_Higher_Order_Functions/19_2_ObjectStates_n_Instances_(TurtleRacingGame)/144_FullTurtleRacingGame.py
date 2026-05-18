from turtle import Turtle, Screen
import random

#%% Setting Up

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

turtle_list = []

#%% Create Turtles

for i in range(6):
    # turtle_list[i] = Turtle(shape="Turtle")  # IndexError: list assignment index out of range
    new_turtle = Turtle(shape="turtle")
    turtle_list.append(new_turtle)
    turtle_list[i].color(colors[i])
    turtle_list[i].penup()
    turtle_list[i].goto(x=-230, y = -125 + i*50)

#%% Off to the Races

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:  # 乌龟大小40x40，xcor()获取的是它中心点的坐标。也就是说当中心点碰到230时，头正好碰到250，所以获胜
            is_race_on = False
            winner_color = turtle.pencolor()  # color好像是同时返回乌龟的颜色和fillingcolor？不懂。所以要specify pencolor
            if user_bet is winner_color:
                print(f"You win. The winner turtle is {winner_color}!")
            else:
                print(f"You lose. The winner turtle is {winner_color}.")
        distance = random.randint(0, 10)
        turtle.forward(distance)


screen.exitonclick()

