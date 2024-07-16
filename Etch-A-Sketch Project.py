from turtle import Turtle, Screen

tim = Turtle()
tim.pensize(3)
screen = Screen()

# Create the turtle for writing the title
title_turtle = Turtle()
title_turtle.hideturtle()
title_turtle.penup()
title_turtle.goto(0, screen.window_height()//2 - 40)
title_turtle.write("Etch A Sketch - Python Version", align="center", font=("Arial", 24, "bold"))

# Create the turtle for writing the controls
title_turtle = Turtle()
title_turtle.hideturtle()
title_turtle.penup()
title_turtle.goto(0, screen.window_height()//2 - 80)
title_turtle.write("Controls: WASD and C for Clear Screen", align="center", font=("Arial", 20, "bold"))


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
