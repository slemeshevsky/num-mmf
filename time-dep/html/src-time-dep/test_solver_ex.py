# -*- coding: utf-8 -*-
import numpy as np
from parab1d import solver_Ex

def test_scalar():
    # Определяем u_exact, f, I
    import sympy as sp
    x, t, a, L = sp.symbols('x t a L')
    u = x*(L-x)*5*t

    def pde(u):
        return sp.diff(u, t) - a*sp.diff(u, x, x)

    f = sp.simplify(pde(u))
    a = 0.5
    L = 1.5

    u_exact = sp.lambdify([x, t], u.subs('L', L).subs('a', a), modules='numpy')
    f = sp.lambdify([x, t], f.subs('L', L).subs('a', a), modules='numpy')
    I = lambda x: u_exact(x, 0)

    h = L/3.
    F = 0.5
    tau = F*h**2/a

    u, x, t, cpu = solver_Ex(I=I, a=a, f=f, L=L, tau=tau, F=F, T=2,
                             user_action=None, version='scalar')
    u_e = u_exact(x, t[-1])
    diff = abs(u_e - u).max()
    tol = 1E-14
    msg = 'Максимальная ошибка solver_Ex, scalar: {}'.format(diff)
    assert diff < tol, msg

def test_vectorized():
    # Определяем u_exact, f, I
    import sympy as sp
    x, t, a, L = sp.symbols('x t a L')
    u = x*(L-x)*5*t

    def pde(u):
        return sp.diff(u, t) - a*sp.diff(u, x, x)

    f = sp.simplify(pde(u))
    a = 0.5
    L = 1.0

    u_exact = sp.lambdify([x, t], u.subs('L', L).subs('a', a), modules='numpy')
    f = sp.lambdify([x, t], f.subs('L', L).subs('a', a), modules='numpy')
    I = lambda x: u_exact(x, 0)

    h = L/10.
    F = 0.5
    tau = F*h**2/a

    u, x, t, cpu = solver_Ex(I=I, a=a, f=f, L=L, tau=tau, F=0.5, T=2,
                             user_action=None, version='vectorized')
    u_e = u_exact(x, t[-1])
    diff = abs(u_e - u).max()
    tol = 1E-14
    msg = 'Максимальная ошибка solver_Ex, vectorized: {}'.format(diff)
    assert diff < tol, msg

def convergenes_rates(u_exact, I, f, a, L, delta0, num_meshes, F, T):
    # В начале определим функцию, которая будет использоваться как user_action
    global error
    error = 0.  # погрешность вычисленная в функции обратного вызова user_action

    def compute_error(u, x, t, n):
        global error  # должна определяться как global для изменения перемнной
        # внутри данной функции, в противном случае переменная error будет
        # локальной и будет отличаться от переменной из внешней функции
        if n == 0:
            error = 0.
        else:
            error = max(error, np.linalg.norm(u - u_exact(x, t[n]), np.inf))

    # Уменьшаем параметр дискретизации и вычисляем погрешности
    E = []
    delta = []
    tau = delta0
    for i in range(num_meshes):
        solver_Ex(I=I, f=f, a=a, L=L, tau=tau, F=F, T=T,
                  user_action=compute_error)
        E.append(error)
        delta.append(tau)
        tau /= 2

    print('E: {}'.format(E))
    # Вычисляем порядки сходимости для двух соседних экспериментов
    r = [np.log(E[i]/E[i-1])/np.log(delta[i]/delta[i-1]) for i in range(1, num_meshes)]
    return r

def test_convrate():
    import sympy as sp
    x, t, a, L = sp.symbols('x t a L')
    u = sp.exp(-sp.pi**2*a*t)*sp.sin(sp.pi*x)

    def pde(u):
        return sp.diff(u, t) - a*sp.diff(u, x, x)

    f = sp.simplify(pde(u))
    a = 0.5
    L = 1

    u_exact = sp.lambdify([x, t], u.subs('L', L).subs('a', a), modules='numpy')
    f = sp.lambdify([x, t], f.subs('L', L).subs('a', a), modules='numpy')
    I = lambda x: u_exact(x, 0)

    h = L/10.
    F = 0.5
    tau = F*h**2/a

    r = convergenes_rates(
        u_exact=u_exact, I=I, f=f, a=a, L=L,
        delta0=tau, num_meshes=6, F=F, T=2.
    )
    success = abs(r[-1] - 1) < 0.002
    msg = 'Погрешности решения: {}'.format()
    assert success, msg

# End
