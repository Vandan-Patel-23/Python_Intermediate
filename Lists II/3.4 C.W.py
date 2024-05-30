# list = ['a', 'b', 'c', 'e', 'f']
# list.append('g') # notice we DO NOT write list =list.append('g')
# print(list)

# list.insert(3, 'd') # insert item 'd' at index 3
# print(list)

# list.extend(list) # extend needs a list as input!
# print(list)

# list.remove('b') # remove the ITEM 'b' from the list
# print(list)

# x = list.pop(1) # remove item at INDEX 1, and store item in x
# print(x)
# print(list)

# list.sort() # now our list is sorted
# print(list)

# list.reverse() # now our list is reversed
# print(list)

# student = "Leo"
# student.upper()
# print(student)

# lst1=[1,8,'House']
# lst2=['12',9,'Japan']


# print(lst1+lst2)

# 1
#it will print none

# 2
# It will mutate lines 2

# 3
Animals= ['Lion', 'Tiger', 'Zebra', 'Sloth', 'Pig']
Animals.insert(1,'Chameleon')
Animals.sort()
Animals.pop(5)
print(Animals)
for i in range(len(Animals)):
    Animals[i] = Animals[i] + '!'
    print(Animals[i])
print(Animals)
print("chameleon" + "!")

best_friends=Animals[:2]

# 1st main difference between list and strings are that strings are not mutable. 2nd main diffence is when we use string methods they use an equal sign but list methods do not allow equal signs.
# Mutablity means to change something. It could be changed when the data type is mutable