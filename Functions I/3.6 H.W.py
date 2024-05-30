import turtle
import random
t = turtle.Turtle()

def draw_rectangle():
    for i in range(2):  
        t.forward(100)
        t.left(90)
        t.forward(50)
        t.left(90)
# draw_rectangle()

def draw_colour_triangle(color):
    t.pencolor(color)
    for _ in range(3):
        t.forward(50)
        t.left(120)
# draw_colour_triangle("red")
def get_random_colour():
    colours = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black"]
    random_colour = random.choice(colours)
    return random_colour
random_colour_result = get_random_colour()
print('Random colour:', random_colour_result)
t.speed(0)
t.pensize(3)
while True:
    colour=get_random_colour()
    draw_colour_triangle(colour)
    t.left(5)
    draw_rectangle()