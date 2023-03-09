from math import sqrt

print("quatratic function: (a*x^2) + b*x + c")
a = float(input("a:  "))
b = float(input("b:  "))
c = float(input("c:  "))

r = b ** 2-4*a*c
print("value of r=",r)
if r>0:
    num_roots = 2
    x1 = (((-b) + sqrt(r))/(2*a))
    x2 = (((-b) - sqrt(r))/(2*a))
    print("there are 2 roots:%f and %f" % (x1,x2))
elif r == 0:
    num_roots = 1
    x = (-b)/2*a
    print("there is one root:",x)
else:
    num_roots=0
    print("no roots,discriminant<0")
    exit()