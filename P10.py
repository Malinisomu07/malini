n=int(input(""))
pg=0
mk=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(0,n):
        if mk[i]<mk[j]:
            pg=pg+(i+1)
print(pg)
