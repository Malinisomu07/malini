n=str(input(" "))
km=[]
for i in n:
    if i not in km:
        km.append(i)
        #print(i)
    else:
        break
print(len(km))
