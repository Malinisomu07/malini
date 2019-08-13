m,k=list(map(str,input().split()))
g=0
if m==k:
  print(g)
elif len(m)>len(k):
  m=list(m)
  k=list(k)
  for i in range(0,len(k)):
    for i in range(0,len(m)):
      if m[j]==k[i]:
        m.pop(j)
        break
    g=len(m)
    print(g)
else:
    for i in range(0,min(len(m),len(k))):
        if m[i]!=k[i]:
            g=g+1
        if i==min(len(m),len(k))-1:
            g = g + abs((i + 1) - max(len(m), len(k)))
    print(g)
