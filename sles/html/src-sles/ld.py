# -*- coding: utf-8 -*-


import numpy as np


def ld(A):
	"""
	Для симметричной матрицы A вычисляет нижнюю треугольную 
	матрицу L и диагональную матрицу D, такие 
	что A = LDL^T. Элементы a_{ij} замещаются	на l_{ij}, если i > j, 
	и на d_i, если i = j
	"""

	n = len(A)
	LD = np.array(A, float)
	for j in range(n):
		v = np.zeros(j+1)
		v[:j] = LD[j,:j]*LD[range(j),range(j)]
		v[j] = LD[j,j] - np.dot(LD[j,:j],v[:j])
		LD[j,j] = v[j]
		LD[j+1:,j] = (LD[j+1:,j] - np.dot(LD[j+1:,:j],v[:j]))/v[j]

	return LD

def ld_solve(A, b):
	"""
	Решает систему Ax = b c использованием LDL^T-разложения
	"""
	LD = ld(A)
	b = np.array(b,float)
	for i in range(1, len(b)):
		b[i] = b[i] - np.dot(LD[i,:i],b[:i])
	b[:] = b[:]/LD[range(len(b)),range(len(b))]
	for i in range(len(b)-1, -1, -1):
		b[i] = (b[i] - np.dot(LD[i+1:,i],b[i+1:]))
	return b

def application():
	A = np.array([[10, 20, 30], [20, 45, 80], [30, 80, 171]])
	print(A)
	print(ld(A))
	x = np.array([1, 1, 1],float)
	b = np.dot(A,x)
	x_s = ld_solve(A,b)
	
	print("exact = " + str(x))
	print("solved = " + str(x_s))
	x

if __name__ == "__main__":
	application()
