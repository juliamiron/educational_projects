#С клавиатуры вводятся три числа a, b, c - коэффициенты квадратного уравнения a*x^2 + bx + c = 0
#Вывести корни этого уравнения или напечатать, что корней нет

import math
a = int(input())
b = int(input())
c = int(input())
D = b**2 - 4*a*c
if D > 0:
  x1 = (-b - math.sqrt(D))/(2*a)
  x2 = (-b + math.sqrt(D))/(2*a)
  print(x1, x2)
elif D == 0:
  x = -b/(2*a)
  print(x)
else:
  print('Корней нет')