import math
def quadratic(a,b,c):
	x=b*b-4*a*c
	x1=(-b+math.sqrt(x))/(2*a)
	x2=(-b-math.sqrt(x))/(2*a)
	return x1,x2
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
