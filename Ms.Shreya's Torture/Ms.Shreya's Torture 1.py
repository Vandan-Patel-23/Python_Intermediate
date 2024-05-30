import turtle
import random

user_sides=int(input('How many sides do you want:'))
sheldon = turtle.Turtle()

colors=["red", "orange", "yellow", "green", "blue", "cyan", "purple", "pink","magenta", "light green", "light blue"]


degree=360/user_sides
size=random.randrange(2,10)
distance=random.randrange(100,300)
sheldon.pensize(size)
for i in range(user_sides):
    color=random.sample(colors,1)
    sheldon.color(color)
    sheldon.forward(distance)
    sheldon.left(degree)