km=int(input())
mk=list(map(int,input().split()))
yz=[1]*km
for i in range(km):
    if i==0:
        if mk[i]>mk[i+1]:
            yz[i]=yz[i]+yz[i+1]
    elif i>0:
        if mk[i]>mk[i-1]:
            yz[i]=yz[i]+yz[i-1]
print(sum(yz))
