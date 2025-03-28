from turtle import Turtle, Screen
from random import randint, choice

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")


colors = ['black', 'red', 'green', 'blue', 'yellow', 'cyan', 'magenta',
          'gray', 'grey', 'maroon', 'purple', 'lime', 'olive', 'navy', 'teal', 'aqua', 'fuchsia', 'silver',
          'darkred', 'indianred', 'lightcoral', 'salmon', 'darksalmon', 'lightsalmon', 'crimson', 'firebrick',
          'darkgreen', 'forestgreen', 'limegreen', 'lightgreen', 'palegreen', 'springgreen', 'mediumseagreen', 'seagreen',
          'olive', 'olivedrab','darkblue', 'mediumblue', 'royalblue', 'skyblue', 'lightskyblue', 'steelblue', 'dodgerblue'
]

def rand_colors():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    color = (r,g,b)
    return color

angle = 0
radius = 100
my_turtle.speed(20)
# Draw a Spirograph

while angle <= 360:
    my_turtle.circle(radius)
    my_turtle.color(choice(colors))
    my_turtle.setheading(my_turtle.heading() + 5)
    angle += 5


# # Draw a Square
# for _ in range(4):
#     my_turtle.forward(100)
#     my_turtle.left(90)
#
# # Draw a discontinue line
# for _ in range(50):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# # Draw geometrical forms
# num_sides = 3
#
# while num_sides < 12:
#
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#
#     num_sides += 1
#     my_turtle.pencolor(choice(colors))

# # Random walk
# direction = [
#     lambda: my_turtle.forward(20),
#     lambda: my_turtle.left(90),
#     lambda: my_turtle.right(90)]
#
# for _ in range(100):
#     my_turtle.pensize(10)
#     my_turtle.speed(10)
#     my_turtle.pencolor(choice(colors))
#     choice(direction)()

screen = Screen()
screen.exitonclick()
