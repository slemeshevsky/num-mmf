# -*- coding: utf-8 -*-

from numpy import linspace
import matplotlib.pyplot as plt

v0 = 5
g = 9.81
t = linspace(0, 1, 1001)

y = v0*t - 0.5*g*t**2

plt.plot(t, y)
plt.xlabel(u't (с)')
plt.ylabel(u'y (м)')
plt.show()

def height(t):
	h =  v0*t - 0.5*g*t**2
	return h

h = lambda t: v0*t - 0.5*g*t**2

