# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

v0 = 5.0
g = 9.81
t = np.linspace(0, 1, 1000)
y = v0*t - 0.5*g*t**2

max_height = y[0]
for i in range(1, 1000):
	if y[i] > max_height:
		max_height = y[i]

print u'Максимальная достигнутая высота равна %f м' % (max_height)

plt.plot(t, y)
plt.xlabel(u'Время (с)')
plt.ylabel(u'Высота (м)')
plt.show()
