import random
from turtle import Turtle, Screen
from game_brain import GameBrain
from random import Random

is_race_on = False
screen = Screen()
screen.bgcolor("pale green")
screen.setup(500, 400)

colors = ["navy", "magenta", "dark goldenrod", "crimson", "purple", "yellow"]
random.shuffle(colors)
y_position = [-120, -70, -20, 30, 80, 130]

tommy = Turtle()

# Function to draw color swatches
def draw_color_swatches():
    tommy.pendown()
    tommy.goto(-150, 0)
    for color_name in colors:
        tommy.color(color_name)
        tommy.begin_fill()
        tommy.forward(30)
        tommy.left(90)
        tommy.forward(30)
        tommy.left(90)
        tommy.forward(30)
        tommy.left(90)
        tommy.forward(30)
        tommy.left(90)
        tommy.end_fill()
        tommy.forward(40)
    tommy.hideturtle()


# Draw color swatches
draw_color_swatches()
user_bet = screen.textinput("Make your bet",
                            f"Which turtle will win the race?\nChoose a lucky color:\n"
                            f"{', '.join(colors)}\n")


if user_bet.lower() in [color.lower() for color in colors]:
    print(f"Your bet is {user_bet}!!")
    all_turtles = []
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.shapesize(1.5)
        new_turtle.penup()
        new_turtle.fillcolor(colors[turtle_index])
        new_turtle.goto(x=-240, y=y_position[turtle_index])
        all_turtles.append(new_turtle)
    game = GameBrain(all_turtles)
    if user_bet:
        is_race_on = True

    while is_race_on:

        for tommy in all_turtles:
            if tommy.xcor() > 220:
                is_race_on = False
                winning_color = tommy.fillcolor()
                # if winning_color == user_bet:
                #     print(f"You've won! The {winning_color} turtle is the winner!!")
                # else:
                #     print(f"You've have lost!! The {winning_color} turtle is winner!!")
                game.guess_winner(user_bet, winning_color)
            rand_distance = random.randint(0, 10)
            tommy.forward(rand_distance)

else:
    print("Invalid color choice!!")

screen.exitonclick()
