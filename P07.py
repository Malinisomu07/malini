import math
n=int(input())
lm=math.log10(n)/math.log10(2)
#print(lm)

#print(math.ceil(lm))
#print(math.floor(lm))
if math.ceil(lm)==math.floor(lm):
	print(0)
else:
	ab=(n-1)//2
	#print(ab)
	bc=ab*2
	#print(bc)
	print(n-bc)
