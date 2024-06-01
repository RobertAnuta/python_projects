# Generate Damien Hirst -  Dot Painting

# import colorgram
from turtle import Turtle, Screen
import turtle
from random import choice

# # Extract 6 colors from an image.
# colors = colorgram.extract('cologram.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     rgb_colors.append((color.rgb[0],color.rgb[1],color.rgb[2]))

# RGB Color list generated with colorgram
color_list = [(227, 230, 236), (243, 236, 242), (244, 239, 226), (235, 243, 239), (194, 166, 108),
              (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34),
              (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24),
              (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135),
              (120, 27, 42), (169, 101, 135), (94, 152, 97), (176, 188, 217), (88, 121, 182),
              (181, 100, 88), (22, 92, 65), (68, 152, 169), (210, 177, 202), (88, 77, 15)]

my_turtle = Turtle()

# Mode to use RGB colors from my list
turtle.colormode(255)

my_turtle.penup()
my_turtle.hideturtle()
my_turtle.goto(-200,-200)
my_turtle.pendown()
x = -200
y = -150


for dot_count in range(1, 101):
    my_turtle.dot(20,choice(color_list))
    my_turtle.penup()
    my_turtle.forward(50)
    my_turtle.pendown()

    if dot_count % 10 == 0:
        my_turtle.penup()
        my_turtle.goto( x,y)
        my_turtle.pendown()
        y += 50


screen = Screen()
screen.exitonclick()