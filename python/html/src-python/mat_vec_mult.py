# -*- coding: utf-8 -*-

from numpy import zeros, mat, transpose

x = zeros(2)
x = mat(x)
x = transpose(x)
x[0] = 1.0; x[1] = 3.0

A = zeros((2,2))
A = mat(A)
A[0,0] = 1.0; A[0,1] = 2.0
A[1,0] = 3.0; A[1,1] = 4.0

y = A*x

print y

