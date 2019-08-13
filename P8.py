import sys, string, math

op,l = input().split()
op,l = int(op),int(l)
km = [ int(x) for x in input().split()]
km.sort()
count = 0
bc = op // 3
for i in range(0,bc) :
    km2 = km[3*i : 3*(i+1)]
    if 5-max(km2) >= l :
        count += 1
print(count)
