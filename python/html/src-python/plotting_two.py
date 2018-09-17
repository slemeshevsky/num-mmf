# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

h = np.zeros(4)

h[0] = 1.60; h[1] = 1.75; h[2] = 1.82; h[3] = 1.72
H = np.zeros(4)
H[0] = 0.60; H[1] = 0.30; H[2] = 1.90; H[3] = 1.99

numbers = np.zeros(4)
numbers[0] = 1; numbers[1] = 2; numbers[2] = 3; numbers[3] = 4

plt.plot(numbers, h, numbers, H)
plt.xlabel(u'Номер по порядку')
plt.ylabel(u'Значение')
plt.show()
