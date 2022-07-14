
a=[[8,3,4],
   [1,5,9],
   [6,7,2]]
i=0
col_0=0
col_1=0
col_2=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==0:
            col_0+=a[i][j]
        elif i==1:
            col_1+=a[i][j]
        elif i==2:
            col_2+=a[i][j]
            column=col_0,col_1,col_2
        j+=1
    i+=1
print("col a[0]:-",col_0)
print("col a[1]:-",col_1)        
print("col a[2]:-",col_2)
print(column)


i=0
a0=0
a1=0
a2=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==0:
            a0+=a[j][i]
        elif i==1:
            a1+=a[j][i]
        elif i==2:
            a2+=a[j][i]
            row=a0,a1,a2
        j+=1
    i+=1
print("row a[0]:-",a0)
print("row a[1]:-",a1)        
print("row a[2]:-",a2)
print(row)

i=0
Dright=0
Lright=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if i==j:
            Dright+=a[i][j]
        if i+j==len(a[i])-1:
            Lright+=a[i][j]
            D=Dright,Lright
        j+=1
    i+=1
print("right D :-",Dright)
print("left D :-",Lright)

if column==row or column== Dright and Lright or row== Dright and Lright:
    print("magic sqare")
else:
    print("wrong")



