# name = "Robert Downey Jr."
# title = "The Iron Giant"
# # name and title are 'global'
# def get_first_word(sentence):
#     space_index = sentence.index(' ')
#     first_word = sentence[:space_index]
#     # space_index, first_word, and sentence only exist here
#     # they are 'local' to this function!
#     # can you print name or title here? Try it out
#     return first_word
# print(sentence)
# print(space_index)
# print(first_word) # what do you think this would print? Try it out
# first_of_title = get_first_word(title)
# print(first_of_title)

# global score : 0
# def check_guess(guess, answer):
#     if guess.lower() == answer.lower():
#         score += 1 # an equals sign means you're reassigning score
# guess1 = input("What is the fastest mammal in the world?")
# check_guess(guess1, "Cheetah")

# def area_square(width):
#     return width * width
# def area_rectangle(width, length):
#     return width * length
# def area_triangle(base, height):
#     return base * height / 2
# def area_circle(?): # what information do you need?
#     return area_circle? # return the area of a circle
# print(area_square(4)) # what is printed?
# print(area_rectangle(6,10)) # what is printed?
# print(?) # call your circle function

# def max(*nums):
#     biggest_so_far = 0 # this only works for positive numbers
#     for num in nums: # nums is a collection!
#         if num > biggest_so_far:
#             biggest_so_far = num
#     return biggest_so_far
# print(max(1,2,34,7))
# print(max()) # what if we give it no arguments? It will give us 0.


# def employee_info(name, position = "Labourer"):
#     print(name, "\t", position)
# # you can give them in any order if you use their names!
# employee_info(position="Supervisor", name="Kira")
# def max(*nums, positive = True):
#     if not positive:
#         return "This function only works for positive numbers!"
#     biggest_so_far = 0 # this only works for positive numbers
#     for num in nums: # nums is a collection!
#         if num > biggest_so_far:
#             biggest_so_far = num
#     return biggest_so_far
# # the collections still must come first
# print(max(1,2,3,4,positive = True))
# print(max(-2,-1,-10, positive = False))

#Own version of the sum function

#Global variable is a variable that can be used anywhere in the program
#Local variable is a variable defined inside a function
#An error will pop up saying "Not Defined"

#min function
# def min(*nums):
#     min_num=nums[0]
#     for num in nums:
#         if min_num>num:
#             min_num=num
#     return min_num

# print(min(3,5,4,36,-1,-20,-10,0))

# def name(*names):
#     for i in names:
#         print(i,end='\t')
# name('lkjhg','kjhgfd','oiuytr','kjhgfd')

# def name_phone():
#     user_name=input('Enter your name(optional):')
#     user_number=input('Enter your phone number(optional)')
#     if len(user_number)>10 or len(user_number)<10:
#         print('The number should be 10 digits long')
#         user_number=input('Enter your phone number(optional)')

#     if user_name=='':
#         user_name+='N/A'
#     if user_number=='':
#         user_number+='xxxxxxxxxx'
#     print(user_name)
#     print(user_number)
# name_phone()

def area(x,y=0):
    if y<=0:
        return x*x
    else:
        return x*y
print(area(20))

def sum_or_product(*numbers,operation):
    if operation==True:
        total=0
        for i in numbers:
            total+=i
        return total
    else:
        counter=1
        for i in numbers:
            counter*=i
        return counter
print(sum_or_product(1,2,3,4,5,6,7,8,9,10,operation=True))
# Optional parameters might be useful when you want a default parameter.
# The advantages of keyword parameters are that you can use them in any order.
# They should be used after the collections if there are any.