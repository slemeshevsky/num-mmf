# -*- coding: utf-8 -*-
from gauss import gauss, gauss_app
import numpy as np

def swap(a, b):
    r = np.zeros_like(a)
    r[:] = a[:]
    a[:] = b[:]
    b[:] = r[:]

def piv_vec(p, b):
    for i in range(len(p)):
        r = b[p[i]]
        b[p[i]] = b[i]
        b[i] = r


def gauss_piv(A):
    n = A.shape[0]
    piv = np.zeros(n-1, int)
    for k in range(n-1):
        mu = int(np.argmax(np.abs(A[k:, k])))
        swap(A[k, k:], A[mu, k:])
        piv[k] = mu

        if A[k, k] != 0:
            t = gauss(A[k:, k])
            A[k+1:, k] = t
            A[k:, k+1:] = gauss_app(A[k:, k+1:], t)

    return piv

def solve(A, b):
    p = gauss_piv(A)
    print("LU с перестановками {}".format(A))
    piv_vec(p, b)
    for i in range(1, len(b)):
        b[i] = b[i] - np.dot(A[i, :i], b[:i])

    for i in range(len(b)-1, -1, -1):
        b[i] = (b[i] - np.dot(A[i, i+1:], b[i+1:]))/A[i, i]


def test_solve():
    A = np.array([[3., 17., 10.], [2., 4., -2.], [6., 18., -12.]])
    x = np.array([1., 1., 1.])
    b = np.dot(A, x)
    print("A = %s\n b = %s" % (A, b))

    solve(A, b)
    print("solution: %s" % (b))


if __name__ == "__main__":
    test_solve()
