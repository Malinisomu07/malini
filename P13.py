km,mk=map(int,input().split())
c=[]
b=[]
a=[int(km) for km in input().split() ]
for i in range(0,mk):
    u,v=map(int,input().split())
    for j in range(u-1 ,v):
        b.append(a[j])
    x=sorted(b)
    c.append(min(b))
    del b[:]
for z in range(0,len(c)):
    print(c[z])
