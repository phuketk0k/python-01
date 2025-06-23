# Solve quadratic equation of form ax^2 + bx + c = 0

# x solves to (-b ± sqrt(b²-4ac))/(2a)

from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))


x = (-b + (b * b - 4 * a * c) ** 0.5) / ( 2 * a)

y= (-b - (b * b - 4 * a * c) ** 0.5) / ( 2 * a)

print("The roots are", x, " and", y)




