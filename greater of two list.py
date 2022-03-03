n=5
a=[]
b=[]
k=0
m=0
for i in range(n):
        ele=int(input())
        a.append(ele)
print(a)        
for i in range(n):
    els=int(input())
    b.append(els)
for i in a:
    k=k+i
for i in b:
    m=m+i
print(b)    
if(k>m):
    print("a is greater") 
else:
    print("b is greater")
