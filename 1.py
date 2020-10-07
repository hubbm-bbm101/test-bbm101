import sys
from math import sqrt
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
delta = b**2 - 4*a*c
if(delta >0):
    print("There are two solutions")
    result1 = (-b + sqrt(delta)) / (2*a)
    result2 = (-b - sqrt(delta)) / (2*a)
    print('Solutions: ' +  str(result1) + ' ' +  str(result2))
elif(delta == 0):
    print("There is only one solution")
    result = -(b/2*a)
    print("Solution: " + str(result))
else:
    print("There is no real solution")

