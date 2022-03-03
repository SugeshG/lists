l=[]
n=int(input("enter the umber of elemets"))
for i in range(0,n):
    ele=int(input())
    l.append(ele)
for i in range(1,n):    
    t=l[i]
    j=i-1
    while(j>=0 and t<=l[j] ):
       l[j+1]=l[j]
       j=j-1
    l[j+1]=t
print(l)        