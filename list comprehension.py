mul=[]
for i in range(1,11):
    mul.append(i*7)
print(mul)    
mul=[i*7 for i in range(1,11)]
print(mul)
names=["sugesh","mimo","sandy","abishek"]
length=[len(name) for name in names]
print(length)             
def odd_numbers(n):
    return[ x for x in range(0,n+1) if x%2!=0]
print(odd_numbers(5))
z=[x for x in range(0,101) if x%3==0]  
print(z)  