#24331A05I6

import math
a=float(input("enter first side of triangle : "))
b=float(input("enter the second side of triangle : "))
c=float(input("enter the third of triangle : "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle : ",area)