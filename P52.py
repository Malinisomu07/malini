    
k1,m1=list(map(int,input().split()))
k2,m2=list(map(int,input().split()))  
k3,m3=list(map(int,input().split()))  
k4,m4=list(map(int,input().split())) 
ab=m2-m1
km=m3-m4
op=k3-k2
rk=k4=k1
if(ab==km==op==rk):
  print("yes")
else:
  print("no")
