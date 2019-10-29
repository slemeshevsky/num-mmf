# -*- coding: utf-8 -*-
import numpy as np

def tri_lu(a, b, c):
    n = len(a)
    d = np.copy(a)
    u = np.copy(b)
    l = np.copy(c)
    u[0] /= d[0] 
    
    for i in range(1, n-1):
        d[i] = d[i] - l[i-1]*u[i-1]
        u[i] = l[i]/d[i]

    d[-1] = d[-1] - l[-1]*u[-1]

    return d, u, l

def solve_lu_tri(a, b, c, f):
    n = len(a)
    d, u, l = tri_lu(a, b, c)
    x = np.zeros(n)
    x[0] = f[0]/d[0]
    for i in range(1, n):
        x[i] = (f[i] - l[i]*x[i-1])/d[i]

    for i in range(n-2, -1, -1):
        x[i] -= x[i+1]*u[i]

    return x

def full_matrix(a, b, c):
    n = len(a)
    res = np.zeros((n, n))
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i==j:
                print(a[i])
            elif j==i-1:
                print(c[i-1])
            elif j==i+1:
                print(b[i+1])
            else:
                print(0.0)
        print('\n')

        

    
def main(n):
    a = 2.*np.ones(n)
    b = -1.*np.ones(n-1)
    c = -1.*np.ones(n-1)
    print(a, b, c)

    h = 1/n
    f = 2*h**2*np.ones(n)
        
    d, u, l = tri_lu(a, b, c)
    print('det(A) = {}'.format(np.product(d)))
#    print('Решение системы: {}'.format(solve_lu_tri(a, b, c)))


if __name__ == '__main__':
    main()
