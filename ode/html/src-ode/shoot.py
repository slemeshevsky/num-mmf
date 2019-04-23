# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from euler import euler, backward_euler

def shooting(f, l, mu1, mu2, h, theta0):
    def y0(theta):
        return np.array([mu1, theta])

    def F(t, u):
        print(u.shape)
        return np.array([u[:, 0], f(t, u[:, 1])])

    def R(theta):
        y, x = euler(F, [y0(theta)], h, l)
        print(y0(theta))
        r = y[-1, 0] - mu2
        return r

    theta = optimize.fsolve(R, theta0)
    y, x = euler(F, [y0(theta)], h, l)
    return y[:, 0], x

#def demo():
def f(t, u):
    return 100*np.ones_like(u) #*u*(u-1)

l = 1.0
mu1 = 0.0
mu2 = 2.0
h = 0.01
u, x = shooting(f, l=l, mu1=mu1, mu2=mu2, h=h, theta0=-10.0)
fig = plt.figure()
l1 = plt.plot(x, u)
fig.legend(l1, 'Solution')
plt.show()

# if __name__ == '__main__':
#     demo()
