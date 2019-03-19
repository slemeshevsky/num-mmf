# -*- coding: utf-8 -*-
import numpy as np
from rk import RK4
import matplotlib.pyplot as plt

def F(t, y):
    return np.array([y[1], -np.sin(y[0])])


t, sol = RK4(F, [1, 0], 0.1, 4*np.pi)
plt.plot(t, sol)
plt.show()
