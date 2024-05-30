
##user_name=input('Enter your name:')
##user_name.upper()

##a='missisauga'
##print(a.count('s'))
##print(a.find('s'))
##
##b='abc@123'
##print(b.isalnum())
##print(b.isalpha())
##print(b.isdigit())
##
##print(b.replace('abc','Vandan'))
##
##c='hi my name is vandan'

#1
##print('A method is similar to a function. There are many types of methods one primarly being string methods.')

#2
##user_name=input('Enter your name:')
##print(user_name[0].upper(),user_name[1:])

#3
##print(user_name.title())

#4
##num = input("What is your favourite number?")
##while num.isdigit() == False:
##    num = input("What is your favourite number?")
##else:
##    num=int(num)
##    print(num,type(num))

##num = input("Enter your choice between 1,2,3,4:")
##while num not in '1234' or len(num)!=1:
##    num = input("Enter ypur choice between 1,2,3,4:")
##else:
##    num=int(num)
##    print(num,type(num))

#5
##num1=input('Enter a number:')
##num2=input('Enter another number:')
##if num1.isdigit() and num2.isdigit():
##    print('The product of the two numbers are', int(num1)*int(num2))

#6
##num1=input('Enter a number:')
##num2=input('Enter another number:')
##while not(num1.isdigit() and num2.isdigit()):
##    num1=input('Enter a number:')
##    num2=input('Enter another number:')
##print('The product of the two numbers are', int(num1)*int(num2))

#7
a='Mow mow mow your boat'.replace('m','r').replace('M','R')
print(a)
