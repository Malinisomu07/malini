a,j=map(int,input().split())
b=list(map(int,input().split()))[:a]
count=0
for i in range(0,len(b)-1):
  for sec in range(i+1,len(b)-1):
    if(b[i]+b[sec]==j):
      count+=1  
if count==1:
  print("yes")
else:
  print("no")
