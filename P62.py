string=str(input(" "))
a=0
b=[]
for i in range(0,len(string)-1):
    for j in range(i+1,len(string)):
        k=string[i:j+1]
        l=k[::-1]
        if k==l:
            b.append(len(string)-len(l))
print(min(b))
