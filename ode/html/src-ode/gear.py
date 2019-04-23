# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def Gear(F, u0, tau, T):
    N_t = int(round(T/tau))
    F_ = lambda t, u: np.asarray(F(t, u))
    t = np.linspace(0, N_t*tau, N_t+1)
    u = np.zeros((N_t+1, len(u0)))
    u[0] = np.array(u0)
    for n in range(3):
        u[n+1] = u[n] + tau*F_(t[n], u[n])

    def Phi(x, v, t):
        return x - tau*F_(t, x) - v

    for n in range(3, N_t):
        u[n+1] = optimize.fsolve(Phi, u[n], args=(u[n], t[n+1]))

    return u, t
    
def demo():
    def F(t, u):
        u1, u2 = u
        return [u2, mu*(1-u1**2)*u2 - u1]

    mu = 50.
    u0 = [2., 0.]
    u, t = Gear(F=F, u0=u0, tau=0.1, T=1.0)
    print('u1={} \n len(u)={}, len(t)={}'.format(u[0, :], len(u[0, :]), len(t)))

    fig = plt.figure()
    l1, l2 = plt.plot(t, u[:, 0], t, u[:, 1])
    fig.legend((l1, l2), ('$u_1$', '$u_2$'))
    plt.show()


if __name__ == "__main__":
    demo()
