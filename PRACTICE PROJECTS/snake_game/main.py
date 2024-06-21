from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set the screen and title
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create a new snake using our class template
snake = Snake()
food = Food()
score = Scoreboard()

# Set the listener
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_points()



screen.exitonclick()
