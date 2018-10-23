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
    error = np.linalg.norm(x_new - x)
    while((error > tol) and (it < max_it)):
        for i in range(len(b)):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:]))/A[i, i]

        error = np.linalg.norm(x_new - x)
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


def test_generate_problem():
    A, b = generate_problem(0.5, 3)
    A_expected = np.array([[2., -1.5, 0.], [-0.5, 2., -1.5], [0., -0.5, 2.]])
    b_expected = np.array([0.5, 0., 1.5])
    matrix_success = (A == A_expected).any()
    b_success = (b == b_expected).any()
    msg = "A = %s, b = %s" % (A, b)

    assert matrix_success and b_success, msg

def test_jacobi():
    A, b = generate_problem(0.5, 3)
    exact = np.linalg.solve(A, b)
    tol = 1e-15
    x, it = jacobi(A, b, tol=tol)
    success = np.linalg.norm(exact - x) < tol
    msg = "exact = %s, approx = %s, number of iterations = %s" % (exact, x, it)

    assert success, msg


if __name__ == "__main__":
    test_jacobi()
