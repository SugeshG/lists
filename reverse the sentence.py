str=input("enter  the sentence :")
words =str.split()
rev_sentence=[]
for i in words:
    i[::-1]
    rev_sentence.append(i[::-1])
j=" ".join(rev_sentence)    
print(rev_sentence)
print(j)
str=input("enter a sentence")
word=str.split()
rev=[]
for i in word:
    i[::-1]
    rev.append(i[::-1])
    j=" ".join(rev)
print(j)    

