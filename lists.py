
print("sugesh")
x=["now","we","are","cooking"]
print(len(x))
print(type(x))
print("sugesh"in x)
print(x)
print(x[len(x)-1])
def get_word(sentence,n):
    if n>0:
        sentence=sentence.split(" ")
        if n<=len(sentence):
            return(sentence[n-1])
        return "  "    
print(get_word("this is a lesson about lists",4))
classroom = ["boys","girls","staff","bench"]
classroom.append("board")
classroom.insert(0,"door")
classroom.remove("girls")
print(classroom.index("door"))
classroom.pop(0)
classroom[2]="girls"
print(classroom,len(classroom))
def skip_elements(elements):
    new_list=[]
    i=0
    for i in range(len(elements)):
        if i%2==0:
            new_list.append(elements[i])
    i=i+1
    return new_list 
print(skip_elements(["a","b","c","d","e","f","g"]))  
print(1%2)       


