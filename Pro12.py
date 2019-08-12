a,b=map(int,input().split())
lis=list(map(int,input().split()))
l=[]
for i in range(0,b):
     u,v=map(int,input().split())
     l.append([u,v])
for i in range(b):
     lower=l[i][0]
     upper=l[i][1]
     s=sum(lis[lower-1:upper])
     print(s)
