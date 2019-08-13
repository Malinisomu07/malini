n,m=map(int,input().split())
tem=[]
x=0
for a in range(n):
    tem.append(list(map(int,input().split())))   
for i in range(n):
    for j in range(m-1):
        for k in range(j+1,m+1):
            if tem[a][j:k]==[1]*len(tem[a][j:k]):
                 if all(tem[p+a][j:k]==[1]*len(tem[p+a][j:k]) for p in range(len(tem[a][j:k])-1)):
                     if len(tem[a][j:k])>x:
                        x=len(tem[a][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for a in range(x):
    print(*[1]*x)
