# -*- coding: utf-8 -*-
import numpy as np

def jacobi(A, b, guess=None, tol=1e-3, max_it=500):
    """
    Решает систему линейных алгебраических уравнений `A * x = b`
    итерационным методом Якоби.

    Параметры
    ---------
    A : (M, M) array_like
         матрица коэффициентов системы;
    b : (M) ndarray
         вектор правой части
    guess : ndarray
          начальное приближение, если None, то нулевой вектор
    tol - точность
    max_it - максимальное число итераций

    Возвращает
    ----------
    x  : (M) ndarray
        вектор решения
    it : int
         число итераций
    """
    x = b.copy()
    x_new = np.zeros_like(b)
    # print("x_new = %s" % (x_new))
    # print("x = %s" % (x))
    if guess is not None:
        x = guess
    it = 0
    r = x_new - x
    error = np.linalg.norm(r)
    while((error > tol) and (it < max_it)):
        for i in range(len(b)):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) -
                        np.dot(A[i, i+1:], x[i+1:]))/A[i, i]

        r = x_new - x
        error = np.linalg.norm(r)
        it += 1
        x[:] = x_new[:]

    return x, it

def generate_problem(alpha, n):
    A = np.zeros((n, n))
    ids = range(n)
    ids_s = np.array(range(n-1))
    A[ids, ids] = 2
    A[ids_s, ids_s + 1] = -1 - alpha
    A[ids_s+1, ids_s] = -1 + alpha

    b = np.zeros(n)
    b[0] = 1 - alpha
    b[-1] = 1 + alpha

    return A, b
