import sys

def Newton(f, dfdx, x, eps):
    f_value = f(x)
    iteration_counter = 0
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            x = x - float(f_value)/dfdx(x)
        except ZeroDivisionError:
            print("Error! - derivative zero for x = " + x)
            sys.exit(1)
        f_value = f(x)
        iteration_counter += 1

    if abs(f_value) > eps:
        iteration_counter = -1
    return x, iteration_counter

def f(x):
    return x**2 - 9
def dfdx(x):
    return 2*x


solution, no_iterations = Newton(f, dfdx, x=1000, eps=1.0e-6)
if no_iterations > 0:
    print("Число вызовов функций: {}".format(1+2*no_iterations))
    print("Решение: {}".format(solution))
else:
    print("Решение не найдено!")
