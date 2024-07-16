from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

# creating the snake body with squares
# turtle1 = Turtle()
# turtle1.shape("square")
# turtle1.color("white")
# turtle2 = Turtle()
# turtle2.shape("square")
# turtle2.color("white")
# turtle3 = Turtle()
# turtle3.shape("square")
# turtle3.color("white")
# screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

for position in starting_positions:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(position)

# positioning the turtles to form the snake body
turtle1.goto(0, 0)
turtle2.goto(-20, 0)
turtle3.goto(-40, 0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()