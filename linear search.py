l=[]
n=5
for i in range(n):
    ele=int(input())
    l.append(ele)
f=0
k=int(input("enter the key:"))
for i in range(0,n):
    if(k==l[i]):
        f=f+1  
if(f==0):
    print("element not found")
else:
    print("element found")              