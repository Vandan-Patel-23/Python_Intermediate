# # with open("files.txt") as rf:
# #     print(rf.readline())
# # open up story.txt on your computer to follow along!
# f = open('files.txt')
# title = f.readline() # this fetches the next line, which is the firstline in the file
# print(title.upper()) # what is printed here?
# for line in f:
#     print(line.strip()) # strip method gets rid of any excess spaces/newlines/tabs
# x = f.read() # what is x? Think of where your cursor is
# f.close()

# with open('files.txt', 'a') as f:
#     f.write('Turning Red') # write will write EXACTLY what you ask
#     f.write('Encanto')

# f = open('files.txt','w')
# name = input("What is your name, user?")
# f.write("last person to run this code is: " + name + "\n")
# f.close()

# candy_names=[]

# with open('C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Intermidiate\\candy_text.txt','r') as cf:
#     for line in cf:
#         a,b=line.split(', ')
#         candy_names.append(a)
#         print(a)
# with open('C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Intermidiate\\long_poem.txt') as f:
#     a=f.readlines()
#     for i in range(0,21,2):
#         print(a[i])

with open('C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Intermidiate\\second_poem.txt') as sp:
    a=sp.readlines()
    for i in a:
        if i != '\n':
            print(i,end='')

