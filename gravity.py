import math
def edge_linger(x,y):
    edge=math.sqrt(x*x+y*y)
    return str(edge)
m=edge_linger(3,4)
print ('the right triangle third side is '+ m)