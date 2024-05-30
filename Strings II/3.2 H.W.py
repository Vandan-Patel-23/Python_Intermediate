#1

#2
money=input('Enter a price for an item:')
b=float(input('How much money are you paying for this item:'))
money_dot_counter=money.count('.')==1
money_dot_index=money.find('.')
whole=money[:money_dot_index]
decimal=money[money_dot_index+1:]
digits=(decimal+whole).isdigit()
front_end=not(money[0]=='.' or money[-1]=='.')
#3
while not (money_dot_counter and digits and front_end):
    print('Make sure there is decimals, numbers only')
    money=input('How much money are you paying for this item(in decimal):')
    money_dot_counter=money.count('.')==1
    money_dot_index=money.find('.')
    whole=money[:money_dot_index]
    decimal=money[money_dot_index+1:]
    digits=(decimal+whole).isdigit()

money=float(money)

print('Your change wll be: %0.2f'%( b-money))
