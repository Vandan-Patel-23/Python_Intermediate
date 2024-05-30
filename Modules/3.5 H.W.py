import turtle
import random

sheldon = turtle.Turtle()
steps = random.randrange(100,300)
degrees = random.randrange(10,350)
colors=["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink","magenta", "light green", "light blue"]
while True:
    color=random.sample(colors,1)
    sheldon.forward(steps)
    sheldon.left(degrees)
    sheldon.color(color)