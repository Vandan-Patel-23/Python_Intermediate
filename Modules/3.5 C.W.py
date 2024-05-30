from datetime import datetime as dt
import math
import random as r
import turtle
shelly = turtle.Turtle()
lst=['Monday', 'Tuesday', 'Wednesday', 'Thusday', 'Friday', 'Saturday', 'Sunday']
a=dt.now().weekday()
print(lst[a])

integer=int(input('Enter a number'))
print(math.sqrt(integer))

employee_lst= ['John', 'Mark', 'Hannah', 'Justin', 'Aarushi', 'Shreya', 'Viraj', 'Manan', 'Chaitali', 'Chair', 'Table', 'Mckeown', 'Rosario', 'Stumpf', 'Cheung']
group_size=int(input('How many people do you need for your job'))
print(r.sample(employee_lst, group_size))

diameter=float(input('Enter a diameter of a circle'))
print('The circumfrence of the circle is', math.pi*diameter)
shelly.color('blue')
for i in range(5):
    shelly.forward(100)
    shelly.left(144)
#it is a Star

# import turtle as t

# def sqaure(size):
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
# sqaure(200)