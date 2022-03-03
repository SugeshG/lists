l=[]
n=int(input("enter the number of elements:"))
for i in range(0,n):
    ele=int(input())
    l.append(ele)
for i in range (0,n):
    for j in range(i+1,n):
        if(l[i]>l[j]):
            t=l[i]
            l[i]=l[j]
            l[j]=t
print(l)            


