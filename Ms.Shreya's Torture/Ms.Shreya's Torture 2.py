def dictionary(key,value, key_to_value):
    key_to_value[key]=value
    return key_to_value
temp = {}
while True:
    user_key=input('Enter a key:')
    user_value=input('Enter a value:')
    temp.update(dictionary(user_key,user_value,temp))
    print(temp)
    user_quit=input('Do you want to exit:')
    if user_quit.lower() == 'yes':
        user_delete_ask=input('Do you want to delete something before you quit:')
        if user_delete_ask.lower() == 'yes':
            user_delete=input('Do you want to delete Key or Value:')
            if user_delete.lower() == 'key':
                key_delete=input('which key would you like to delete:')
                temp.pop(key_delete,None)
            else:
                value_delete=input("which key's value would you like to delete:")
                temp.pop(value_delete, temp[value_delete])
        break
print(temp)
with open('C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\\Vandan\\Python Intermidiate\\list.txt','a') as f:
    for key,value in temp.items():
        f.write(key+':'+value+"\n")