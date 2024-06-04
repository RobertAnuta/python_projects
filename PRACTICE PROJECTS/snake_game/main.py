from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

starting_position = [(0,0), (-20, 0),(-40,0)]

body_length = []

for position in starting_position:
    turtle_body = Turtle(shape="square")
    turtle_body.color("white")
    turtle_body.penup()
    turtle_body.goto(position)
    body_length.append(turtle_body)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    for segment in body_length:







screen.exitonclick()
