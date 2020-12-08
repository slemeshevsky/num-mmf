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

def house(x):
    mu = np.linalg.norm(x)
    v = x.copy()
    if mu != 0:
        beta = x[0] + np.sign(x[0])*mu
        v[1:] = v[1:] / beta
    v[0] = 1.

    return v

def givens(a, b):
    if b == 0:
        c = 1.
        s = 0.
    else:
        if np.abs(b) > np.abs(a):
            t = -a/b
            s = 1./np.sqrt(1 + t**2)
            c = s*t
        else:
            t = -b/a
            c = 1./np.sqrt(1 + t**2)
            s = c*t
    return c, s

def row_house(A, v):
    beta = -2./np.dot(v, v)
    w = beta*np.dot(A.T, v)
    A += np.outer(v, w)

def col_house(A, v):
    beta = -2./np.dot(v, v)
    w = beta*np.dot(A, v)
    A += np.outer(w, v)

def row_rot(A, c, s):
    q = A.shape[1]
    for j in range(q):
        t1 = A[0, j]
        t2 = A[1, j]
        A[0, j] = c*t1 - s*t2
        A[1, j] = s*t1 + c*t2

def col_rot(A, c, s):
    q = A.shape[0]
    for i in range(q):
        t1 = A[i, 0]
        t2 = A[i, 1]
        A[i, 0] = c*t1 - s*t2
        A[i, 1] = s*t1 + c*t2

def house_transfrom(A):
    n = A.shape[0]
    for k in range(n-1):
        v = house(A[k+1:, k])
        row_house(A[k+1:, k:], v)
        col_house(A[:, k+1:], v)

def qr_wilkinson_step(T):
    n = T.shape[0]
    d = (T[-2, -2] - T[-1, -1])/2.
    mu = T[-1, -1] - T[-1, -2]**2/(d + np.sign(d)*np.sqrt(d**2 + T[-1, -2]))
    x = T[0, 0] - mu
    z = T[1, 0]
    for k in range(n-1):
        c, s = givens(x, z)
        S = T[[k, k+1], :]
        row_rot(S, c, s)
        T[[k, k+1], :] = S
        S = T[:, [k, k+1]]
        col_rot(S, c, s)
        T[:, [k, k+1]] = S
        if k < n-2:
            x = T[k+1, k]
            z = T[k+2, k]

def sym_qr(A, eps):
    T = house_transfrom(A)
    n = A.shape[0]
    q = 0
    while(q != n):
        for i in range(n):
            if np.abs(A[i, i+1]) <= eps*(np.abs(A[i, i]) + np.abs(A[i+1, i+1])):
                A[i, i+1] = 0.
                A[i+1, i] = 0.
            

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
    for n in [8, 32, 128, 512, 720]:
        H = generate_hilbert(n)
        l, x = degree(H)
        print("n = %d: lambda = %f" % (n, l))


if __name__ == "__main__":
    application()
