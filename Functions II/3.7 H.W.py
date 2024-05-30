#1
def Sum(*sums):
    counter=0
    for i in sums:
        counter+=i
    return(counter)

print(Sum(1,2,3,4,5,6,7,8,9,10))

#2
def Length(lenghts):
    counter=0
    for i in lenghts:
        counter+=1
    return(counter)
print(Length('How are you doing today'))

#3
def range(end_p,strat_p=0,steps=1):
    lst=[]
    counter=strat_p
    while counter<end_p:
        lst.append(counter)
        counter+=steps
    return(lst)
print(range(14))

def slicing(lst,start=0,end=-1,step=1):
    if end==-1:
        lst_sliced=[]
        end=len(lst)-1
        counter=lst[start]
        while start<end+1:
            lst_sliced.append(counter)
            start+=step
            counter=lst[start]
        return(lst_sliced)
    else:
        lst_sliced=[]
        counter=lst[start]
        while start<end+1:
            lst_sliced.append(counter)
            start+=step
            counter=lst[start]
        return(lst_sliced)
print(slicing([6,7,3,8,9,66,99],2,5))

name='Vraj'
#1. counter 2.lst 3.Lenghts