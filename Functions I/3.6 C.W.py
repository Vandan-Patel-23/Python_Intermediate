# import turtle as t # we can write t instead of the module name
# harold = t.Turtle() # create turtle object

# harold.speed(0)
# colours = ["light green", "green", "blue", "purple", "blue","green"]
# current_colour = 0 #this keeps track of where we are in the list
# for i in range(72):
#     if current_colour == len(colours):
#         current_colour = 0 # send us back to start of the list
#     harold.color(colours[current_colour])
#     harold.circle(100) # this method has harold draw a circle
#     harold.left(5)
#     current_colour += 1

#No parameter and no return value
# def add():
#     a = int(input('Enter a number:'))
#     b = int(input('Enter another number:'))
#     ans=a+b
#     print(ans)
# # add()

# #no paramter return value function
# def sub():
#     a = int(input('Enter a number:'))
#     b = int(input('Enter another number:'))
#     ans=a-b
#     return ans

# # print(sub())
# # a=sub()
# # print(a)

# #parameter no return value
# def mul(a,b):
#     ans=a*b
#     print(ans)
# # int1 = int(input('Enter a number:'))
# # int2 = int(input('Enter another number:'))
# # mul(int1,int2)

# #parameter return value     
# def pow(b,e):
#     ans=1
#     for i in range(e):
#         ans*=b
#     return ans
# # base = int(input('Enter a base:'))
# # exp = int(input('Enter an exponent:'))
# # a=pow(base,exp)
# # print(a)

# # base = int(input('Enter a base:'))
# # exp = int(input('Enter an exponent:'))
# # print(pow(base,exp))



# def print_helpinfo():
#     print("Welcome to Brick Breaker 3000")
#     print("--------CONTROLS-------")
#     print("\tUse arrow keys to move!")
#     print("\tUse space to shoot!")
# print_helpinfo()

# def print_player_data(username, highscore, attempts):
#     print("PLAYER NAME: ", username)
#     print("has a highscore of: ", highscore)
#     print("after a total of", attempts, "attempts")
# print_player_data("2Cool4School", 125, 10)
# print_player_data("JUnKR@T", 250, 18)

# def brick_points(type):
#     if type == "common":
#         points = 10
#     elif type == "rare":
#         points = 50
#     elif type == "legendary":
#         points = 100
#     return points # points is what is returned
# score = 0
# # hit a common brick, that's 10 points - add this value to score
# score = score + brick_points("common")

# def print_triangle(): # since its task is to print a triangle
#     for i in range(5): # it does not need any input, or give output
#         print("@" * i)
#     print_triangle()
# print_triangle()


def print_triangle():
    for i in range(5):
        print("@" * i)
print_triangle()
def ask_silly_question():
    input("Press any key to continue: ")
ask_silly_question()
ask_silly_question()
import random
def guess_my_number(): 
    my_number = random.randrange(1,10)
    guess = int(input("Guess a number between 1 and 10! "))
    if guess == my_number:
        print("You guessed it right!")
    else:
        print("Wrong! My number was", my_number)
guess_my_number()
guess_my_number()

def double(x): # our parameter is x, which can be anything
    print(x * 2) # we do NOT write a number as our parameter
double(4) # we write the number when we CALL it, as the argument
def print_stars(number_of_stars): # use descriptive parameter names
    print("*" * number_of_stars)
print_stars(5)
# what would happen if I wrote: print_stars("ten") ?
def print_ticket_price(type, discount):
    if type == "child":
        print("Child tickets cost $3.99")
    elif type == "senior":
        print("Senior tickets cost $5.49")
    elif discount: # we expect discount to always be True or False
        print("Adult ticket with Family Discount is $6.25")
    else:
        print("Adult ticket, no discount, costs $7.25")
print_ticket_price("senior", False)
print_ticket_price("adult", True)
# what happens when you call this function with 1 argument? 

def get_sum(x, y):
    return x + y
print(get_sum(10,15)) # what will this print?
def is_adult(age):
    if age > 17:
        return True
    else:
        return False
# this function has multiple return statements, but you can see that
# no matter what argument is passed in for 'age', it always returns
# just one value. There is no way the code can reach both returns!
a = is_adult(89) # what is stored in variable a?
if is_adult(10): # if is adult(10) evaluates to True, it will print
    print("10 year olds are adults") # will this be printed?
user_age = int(input("How old are you?" ))
if is_adult(user_age): # it only prints if they enter 18 or higher
    print("You are an adult.")
is_adult(99) # where is the return value going here?