# with open('C:\\Users\\ucbra\\OneDrive\\Desktop\\UC Academy\Vandan\\Python Intermidiate\\allcoders.txt','a') as ac:
#     a=input('Enter your name:')
#     ac.write(a)
#     ac.write('\n')

f = open('file_knowledges.txt','w')
f.write('A file object is an interface between the progrom and the file')
f.close()

d = open('pattern.txt', 'w')
for i in range(10, 0, -1):
    d.write('*'*i + "\n")
d.close()

    
        