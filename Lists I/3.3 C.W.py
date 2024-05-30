password = "U1tra_Secret_P@ssw0rd"
c = 0
s = 0
d = 0
for character in password:
    if not (character.isalnum()):
        s += 1
    elif not character.isalpha() and character.isalnum():
        d += 1
    elif character.isupper():
        c += 1
if c >= 2 and d >= 2 and s >= 2:
    print("That's a strong password!")
else:
    print("You should try to make a stronger password!")
print('c represents the amount of upper letters. s represents the amount of characters that are not numbers and letters. d represents the amount of characters that are not letters and numbers')

lst=[]
print(lst)
lst=[1,2,3,4,5]
print(lst)
lst=[2.2,4,7.7,45]
print(lst)
lst=['hi','hello',2,5,6.8]
print(lst[1])
lst[1]=1.1
print(lst)

class_votes=["Jen", "Jayden", "Jared", "Jen", "Jen", "Jayden", "Jayden", "Jen"]
counter=0
for i in class_votes:
    if i=='Jen':
        counter=counter+1
print(counter)
Jayden=class_votes.count('Jared')
Jared=class_votes.count('Jayden')
print(Jayden)
print(Jared)

if counter>Jayden and Jared:
    print('The winner is Jen with',counter,'votes')

friends_names = ["jeremy", "jason", "jaymit", "river", "lily", "jen", "ben", "harley", "frida"]
friends_names+=['lisa', 'prisha', 'nathan']
print(friends_names)
count=0
for name in friends_names:
    if name[0] == 'j':
        count+=1
print('There are',count,'that start with the letter J')

for name in friends_names:
    print(name[0].upper() + name[1:])
    

