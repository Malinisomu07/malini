a=int(input())
kumarmalu=list(map(int,input().split()))
km=[]
mk=1
for i in range(a):
  v=kumar[i:]
  ans=len(v)
  for j in range(ans-1):
    if v[j]>0 and v[j+1]<0:
      mk=mk+1
    elif v[j]<0 and v[j+1]>0:
      mk=mk+1
    else:
      break
  km.append(str(mk))
  mk=1
print(" ".join(km))
