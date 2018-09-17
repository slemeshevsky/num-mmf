# -*- coding: utf-8 -*-

import numpy as np

v0 = 4.5
g = 9.81
t = np.linspace(0, 1, 1000)
y = v0*t - 0.5*g*t**2

i = 0
while y[i] >= 0:
	i += 1

print u'y = 0 в момент времени ', 0.5*(t[i-1] + t[i])

import matplotlib.pyplot as plt

plt.plot(t, y)
plt.xlabel(u'Время (с)')
plt.ylabel(u'Высота (м)')
plt.show()
