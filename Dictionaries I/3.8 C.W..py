#Before Classwork Homework
first_to_lastname = {'Vandan':'Patel','Shreya':'Pandya','Nithesh':'Nimalraj','Rajdeep':'Yanamalachintala'}
print(first_to_lastname['Vandan'])
print(first_to_lastname['Shreya'])
print(first_to_lastname['Nithesh'])
print(first_to_lastname['Rajdeep'])

movie_to_rating = {'Bee Movie':4,'Harry Potter':10,'Captin Underpants':9,'Toy Story 3':8}
print('My rating out of 10 is:',movie_to_rating['Bee Movie'])
print('My rating out of 10 is:',movie_to_rating['Harry Potter'])
print('My rating out of 10 is:',movie_to_rating['Captin Underpants'])
print('My rating out of 10 is:',movie_to_rating['Toy Story 3'])

countries_to_capital = {'Canada':"Ottawa",'United States of America':'Washington D.C'}
print(countries_to_capital['Canada'])
print(countries_to_capital['United States of America'])

#Classwork Homework
family_to_ages = {'BOB the BUILDER':2,'Spongbob':13,'Captin':20,'Dog':30}
print(family_to_ages['BOB the BUILDER'])
print(family_to_ages['Spongbob'])
print(family_to_ages['Captin'])
print(family_to_ages['Dog'])

name_to_height = {}
name_to_height['Samantha']=3
name_to_height['Natalie']=2
name_to_height['Amy']=1

cities = ['Prague', 'Kyvev', 'Lisbon', 'Lagos','Minneapolis', 'Nice', 'Kitchener']

mt_dictionary = {} # change the name
for item in cities: # change item and collection here
    mt_dictionary[item] = len(item) # fix this line
print(mt_dictionary)

words = ["banana", "apple", "kiwi", "papaya"]
num_a = [3,1,0,3]
emty_dict={}
for i in range(len(words)):
    emty_dict[words[i]]= num_a[i]
print(emty_dict)



def dictionary(key,value, key_to_value):
    key_to_value[key]=value
    return key_to_value
temp = {}
while True:
    
    user_key=int(input('Enter a key:'))
    user_value=input('Enter a value:')
    user_quit=input('Do you want to exit:')
    if user_quit == 'Yes':
        break
    
    temp.update(dictionary(user_key,user_value,temp))
print(temp)



# while True:
#     user_key=int(input('Enter a key'))
#     user_value=input('Enter a value')
#     user_quit=input('Do you want to exit')
#     key_to_value[user_key]=user_value
#     print(key_to_value)
#     if user_quit == 'Yes':
#         print(key_to_value)
#         break
