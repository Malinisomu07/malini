a,b=map(int,input().split())
lis=list(map(int,input().split()))
a=[]
lis.insert(0,0)
for i in range(b):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for j in range(cc,dd+1):         
         sumup^=lis[j]     
     a.append(sumup)
for c in a:
    print(c)
