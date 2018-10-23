# -*- coding: utf-8 -*-
import numpy as np

def cg(A, b, tol, it_max):
    it = 0
    x = 0
    r = np.copy(b)
    r_prev = np.copy(b)
    rho = np.dot(r, r)
    p = np.copy(r)
    while (np.sqrt(rho) > tol*np.sqrt(np.dot(b, b)) and it < it_max):
        it += 1
        if it == 1:
            p[:] = r[:]
        else:
            beta = np.dot(r, r)/np.dot(r_prev, r_prev)
            p = r + beta*p
            w = np.dot(A, p)
            alpha = np.dot(r, r)/np.dot(p, w)
            x = x + alpha*p
            r_prev[:] = r[:]
            r = r - alpha*w
            rho = np.dot(r, r)

    return x, it

