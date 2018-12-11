# -*- coding: utf-8 -*-
import numpy as np
from newton import Newton, Newton_system

def test_Newton():
    from sympy import symbol, diff, lambdify

    x = symbol.Symbol('x')       # определяем математический символ x
    f_expr = x**2 - 4            # символьное выражение для f(x)
    dfdx_expr = diff(f_expr, x)  # вычисляем символьно f'(x)

    # Преобразуем f_expr и dfdx_expr в обычные функции Python
    f = lambdify([x],            # аргумент f
                 f_expr)
    dfdx = lambdify([x], dfdx_expr)

    tol = 1e-3
    computed, no_iterations = Newton(f, dfdx, x=1, eps=tol)
    expected = 2.
    success = np.abs(computed - expected) <= tol
    msg = 'expected = {},\n computed = {}, Число итераций = {}'.format(expected, computed, no_iterations)
    assert success, msg


def test_Newton_system():
    def F(x):
        y = np.zeros_like(x)
        y[0] = (3 + 2*x[0])*x[0] - 2*x[1] - 3
        y[1:-1] = (3 + 2*x[1:-1])*x[1:-1] - x[:-2] - 2*x[2:] - 2
        y[-1] = (3 + 2*x[-1])*x[-1] - x[-2] - 4
        return y

    def J(x):
        n = len(x)
        jac = np.zeros((n, n))
        jac[0, 0] = 3 + 4*x[0]
        jac[0, 1] = -2
        for i in range(n-1):
            jac[i, i-1] = -1
            jac[i, i] = 3 + 4*x[i]
            jac[i, i+1] = -2
        jac[-1, -2] = -1
        jac[-1, -1] = 3 + 4*x[-1]

        return jac

    n = 10
    guess = 3*np.ones(n)
    tol = 1e-3
    computed, its = Newton_system(F, J, guess)
    expected = np.ones_like(guess)
    success = np.linalg.norm(expected-computed) < tol
    msg = 'expected = {},\n computed = {}, iteration_counter={}'.format(expected, computed, its)
    assert success, msg
