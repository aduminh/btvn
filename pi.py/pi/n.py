import math
from math import pi
from math import sqrt
def basel(a):
    phuongtrinh=0
    b=0
    step=0
    while(pi-sqrt(phuongtrinh))>a:
        b+=1
        phuongtrinh+=(1/(b**2))*6
        step+=1
    return sqrt(phuongtrinh),step
print(basel(0.1))
 
     