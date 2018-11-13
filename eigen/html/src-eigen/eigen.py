# -*- coding: utf-8 -*-
import numpy as np
from gauss import inverse

def degree(A, tol=1e-3, max_it=500):
    it = 0
    q = np.zeros(A.shape[0], float)
    q[0] = 1.
    lmbda = np.dot(np.dot(A, q), q)
#    print(lmbda)
    error = np.abs(lmbda)
    while((error > tol) and (it <= max_it)):
        q = np.dot(A, q)
        q /= np.linalg.norm(q)
        lmbda_prev = lmbda
        lmbda = np.dot(np.dot(A, q), q)
        error = np.abs(lmbda - lmbda_prev)
        it += 1
    return lmbda, q

def inverse_degree(A, tol=1e-3, max_it=500):
    it = 0
    q = np.zeros(A.shape[0], float)
    q[0] = 1.
    A_inv = inverse(A)
    lmbda = np.dot(np.dot(A_inv, q), q)
#    print(lmbda)
    error = np.abs(lmbda)
    while((error > tol) and (it <= max_it)):
        q = np.dot(A_inv, q)
        q /= np.linalg.norm(q)
        lmbda_prev = 1./lmbda
        lmbda = 1./np.dot(np.dot(A_inv, q), q)
        error = np.abs(lmbda - lmbda_prev)
        it += 1
    return lmbda, q

def test_degree():
   A = np.array([[-261, 209, -49],
                 [-530, 422, -98],
                 [-800, 631, -144]], float)
   tol = 1e-3
   computed, x = degree(A, tol=tol)
   expected = 10.
   error = np.abs(computed - expected)
   success = error <= tol
   msg = "computed = %f, expected = %f, error = %f" % (computed, expected, error)
   assert success, msg

def test_inverse_degree():
   A = np.array([[-261, 209, -49],
                 [-530, 422, -98],
                 [-800, 631, -144]], float)
   tol = 1e-3
   computed, x = inverse_degree(A, tol=tol)
   expected = 3.
   error = np.abs(computed - expected)
   success = error <= tol
   msg = "computed = %f, expected = %f, error = %f" % (computed, expected, error)
   assert success, msg

def generate_hilbert(n):
    return np.array([[1./(i+j+1) for i in range(n)] for j in range(n)])

def application():
    for n in range(2, 11):
        H = generate_hilbert(n)
        l, x = degree(H)
        print("n = %d: lambda = %f" % (n, l))


if __name__ == "__main__":
    application()
