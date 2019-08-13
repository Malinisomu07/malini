import sys, string, math
def reduM( o, p) :
	if p <= 0 : return o

	if o == 0 : return 10	# Fail
	k1= reduM(o//10, p)*10 + o%10
	k2 = reduM(o//10, p-1)
	if k1 < k2 :
		return k1
	else :
		return k2

o,p = input().split()
o,p = int(o),int(p)
print(reduM(o,p))
