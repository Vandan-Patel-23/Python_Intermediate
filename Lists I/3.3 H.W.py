lst=['Hello', 'Zebra', 'Mount', 'House']
user_add=input('Would you like to add to the list')

while user_add == 'yes':
    user_what_add=input('What would you like to add to the list')
    lst+=user_what_add
    user_modify=input('Would you like to modify your list')
    ind = input('What index would you like to modify your list')
    if user_modify == 'yes' and int(ind) < len(lst)-1:
        lst[int(ind)] =user_what_add
    user_add=input('Would you like to add something else to the list')
print(lst)

#A string is a collection of letters. If you add a number type then it won't store it as a integer. A list can support strings, integers, and floats
#You will get an index error when you enter an index that is larger then the index of the list  