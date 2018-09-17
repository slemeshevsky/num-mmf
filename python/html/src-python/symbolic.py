# -*- coding: utf-8 -*-

from sympy import *

x = Symbol('x')
y = Symbol('y')

print x**2 + 3*y**3
print diff(x**3, x)              # дифференцирование
print integrate(tan(x), x)       # интегрирование
print simplify((x**2+x**3)/x**2) # упрощение выражения
print limit((1+x)**(1/x), x, 0)  # вычисление предела
print solve(x**2-16, x)          # решение уравнения x^2=16
