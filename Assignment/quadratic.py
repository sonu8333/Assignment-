import math
a = 1
b = -5 # for getting solution in positive we should take value of b -(negative)
c = 6
d = b ** 2 - 4 * a *c
#print(d) first we find value of d 
r1 = (- b + d **0.5) / (2 * a) # for r1 we used ** for square root
print(r1)

r2 = (-b - d ** 0.5) / (2 * a) # for r2 we used ** for square root
print(r2)

print("roots are:", r1, "and", r2)
print(f'quadratic equation solution for above {r1} and {r2} ')