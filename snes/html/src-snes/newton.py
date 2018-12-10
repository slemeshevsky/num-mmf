# -*- coding: utf-8 -*-
import numpy as np

def naive_Newton(f, dfdx, x, eps):
    while abs(f(x)) > eps:
        x = x - float(f(x))/dfdx(x)
        print(x)
    return x

def Newton(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - f_value/dfdx(x)
        except ZeroDivisionError as err:
            print("Ошибка: {}".format(err))
            sys.exit(1)
        f_value = f(x)
        iteration_counter += 1

    if abs(f_value) > eps:
        iteration_counter = -1
    return x, iteration_counter

def Newton_system(F, J, x, tol=1e-3):
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)
    iteration_counter = 0
    while F_norm > tol and iteration_counter < 100:
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1

    if F_norm > tol:
        iteration_counter = -1

    return x, iteration_counter


def f(x):
    return x**2
def dfdx(x):
    return 2*x


sol, no_iterations = Newton(f, dfdx, x=1.09, eps=1.0e-6)

if no_iterations > 0:
    print("Число вызовов функций f(x) = x**2: {}".format(1+2*no_iterations))
    print("Решение: {}".format(sol))
else:
    print("Решение не найдено!")

# End 1st ex
# Использование символьных вычислений
from sympy import symbol, tanh, diff, lambdify

x = symbol.Symbol('x')       # определяем математический символ x
f_expr = tanh(x)             # символьное выражение для f(x)
dfdx_expr = diff(f_expr, x)  # вычисляем символьно f'(x)

# Преобразуем f_expr и dfdx_expr в обычные функции Python
f = lambdify([x],            # аргумент f
             f_expr)
dfdx = lambdify([x], dfdx_expr)

tol = 1e-1
sol, its = Newton(f, dfdx, x=1.09, eps=tol)
if no_iterations > 0:
    print("Уравнение: tanh(x) = 0. Число итераций: {}".format(no_iterations))
    print("Решение: {}, eps = {}".format(sol, tol))
else:
    print("Решение не найдено!")
