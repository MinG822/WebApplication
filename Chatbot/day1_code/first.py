li=[]

for n1 in list(range(1,10)):
    li2=[]
    for n2 in list(range(1,10)):
        li2.append(n1*n2)
    li.append(li2)
    
print(li)