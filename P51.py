n=int(input())
kumar=list(map(int,input().split()))
km1=[]
km2=1
for i in range(n):
  v=kumar[i:]
  ans=len(v)
  for j in range(ans-1):
    if v[j]>0 and v[j+1]<0:
      km2=km2+1
    elif v[j]<0 and v[j+1]>0:
      km2=km2+1
    else:
      break
  km1.append(str(km2))
  km2=1
print(" ".join(km1))
