from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win")
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

### y_position = [-100, -60, -20, 20, 60, 100, 140]
### for turtle_index in range(0, 6):
###     new_turtle = Turtle(shape="turtle")
###     new_turtle.color(random.choice(colors))
###     new_turtle.penup()
###     new_turtle.goto(x=-250, y=y_position[turtle_index])
###     all_turtles.append(new_turtle)

tim = Turtle(shape="turtle")
tim.color(random.choice(colors))
tim.penup()
tim.goto(x=-250, y=-100)

tim2 = Turtle(shape="turtle")
tim2.color(random.choice(colors))
tim2.penup()
tim2.goto(x=-250, y=-60)

tim3 = Turtle(shape="turtle")
tim3.color(random.choice(colors))
tim3.penup()
tim3.goto(x=-250, y=-20)

tim4 = Turtle(shape="turtle")
tim4.color(random.choice(colors))
tim4.penup()
tim4.goto(x=-250, y=20)

tim5 = Turtle(shape="turtle")
tim5.color(random.choice(colors))
tim5.penup()
tim5.goto(x=-250, y=60)

tim6 = Turtle(shape="turtle")
tim6.color(random.choice(colors))
tim6.penup()
tim6.goto(x=-250, y=100)

tim7 = Turtle(shape="turtle")
tim7.color(random.choice(colors))
tim7.penup()
tim7.goto(x=-250, y=140)

if user_bet:
    is_race_on = True

all_turtles = [tim, tim2, tim3, tim4, tim5, tim6]

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            print(f"{turtle.pencolor()} turtle won!")
            if turtle.pencolor() == user_bet:
                print("You won!")
            else:
                print("You lost!")

    random_distance = random.randint(0, 10)
    turtle.forward(random_distance)

screen.exitonclick()
