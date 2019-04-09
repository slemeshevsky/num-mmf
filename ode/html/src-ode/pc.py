# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def pc(F, u0, tau, T):
    N_t = int(round(T/tau))
    F_ = lambda t, u: np.asarray(F(t, u))
    t = np.linspace(0, N_t*tau, N_t+1)
    u = np.zeros((N_t+1, len(u0)))
    u[0] = np.array(u0)
    for n in range(3):
        u[n+1] = u[n] + tau*F_(t[n], u[n])

    for n in range(3, N_t):
        p = u[n] + tau/24.*(55.*F_(t[n], u[n]) - 59.*F_(t[n-1], u[n-1]) + 37.*F_(t[n-2], u[n-2]) - 9.*F_(t[n-3], u[n-3]))
        u[n+1] = u[n] + tau/24.*(9*F_(t[n+1], p) + 19*F_(t[n], u[n]) - 5*F_(t[n-1], u[n-1]) + F_(t[n-2], u[n-2]))
    return u, t

def demo_pc():
    def F(t, u):
        u1, u2, u3 = u
        return [u2 - u3, u1 + a*u2, b + u3*(u1 - c)]

    a, b, c = 0.2, 0.2, 2.5
    tau = 0.1
    T = 5.
    u0 = [1., 1., 1.]

    u, t = pc(F=F, u0=u0, tau=tau, T=T)
    fig = plt.figure()
    l1, l2, l3 = plt.plot(t, u[:, 0], t, u[:, 1], t, u[:, 2])
    fig.legend((l1, l2, l3), ('$u_1$', '$u_2$', '$u_3$'))
#    plt.xlabel('часы')
    plt.show()



    
if __name__ == "__main__":
    # demo_population_growth()
    # demo_SIR()
    demo_pc()
