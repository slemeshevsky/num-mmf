# -*- coding: utf-8 -*-
import numpy as np

def gauss(x):
	x = np.array(x,float)
	return x[1:]/x[0]

def gauss_app(C, t):
	C = np.array(C, float)
	t = np.array([[t[i]] for i in range(len(t))], float)
	C[1:,:] = C[1:,:] - t*C[0,:]
	return C

def lu(A):
	LU = np.array(A, float)
	for k  in range(LU.shape[0]-1):
		t = gauss(LU[k:, k])
		LU[k+1:,k] = t
		LU[k:, k+1:] = gauss_app(LU[k:, k+1:], t)
	return LU

def solve_lu(A, b):
	LU = lu(A)
	b = np.array(b,float)
	for i in range(1,len(b)):
		b[i] = b[i] - np.dot(LU[i,:i],b[:i])
	for i in range(len(b)-1, -1, -1):
		b[i] = (b[i] - np.dot(LU[i,i+1:],b[i+1:]))/LU[i,i]
	return b

def test_solve_lu():
	A = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 10]])
	expected = np.array([-1./3, 1./3, 0])
	b = np.dot(A, expected)
	computed = solve_lu(A,b)
	tol = 1e-14
	success = np.linalg.norm(computed - expected) < tol
	msg = 'x_exact = ' + str(expected) + '; x_computed = ' + str(computed)
	assert success, msg

def application():
	A = np.array([[1, 4, 7], [2, 5, 8], [3, 6, 10]])
	x = np.array([-1./3, 1./3, 0])
	b = np.dot(A, x)
	x_computed = solve_lu(A, b)
	print 'computed =', x_computed, 'exact = ', x

if __name__ == '__main__':
	application()
