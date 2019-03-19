# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def euler(F, u0, tau, T):
    N_t = int(round(T/tau))
    F_ = lambda t, u: np.asarray(F(t, u))
    t = np.linspace(0, N_t*tau, N_t+1)
    u = np.zeros((N_t+1, len(u0)))
    u[0] = np.array(u0)
    for n in range(N_t):
        u[n+1] = u[n] + tau*F_(t[n], u[n])

    return u, t

def demo_population_growth():
    def F(t, u):
        return 0.1*u

    u, t = euler(F=F, u0=[100], tau=0.5, T=20)
    plt.plot(t, u, t, 100*np.exp(0.1*t))
    plt.show()

def demo_SIR():
    def F(t, u):
        S, I, R = u
        return [-beta*S*I, beta*S*I-gamma*I, gamma*I]

    beta = 10./(40*8*24)
    gamma = 3./(15*24)
    tau = 0.1
    D = 30
    N_t = int(D*24/tau)
    T = tau*N_t
    u0 = [50, 1, 0]

    u, t = euler(F=F, u0=u0, tau=tau, T=T)
    S = u[:, 0]
    I = u[:, 1]
    R = u[:, 2]
    fig = plt.figure()
    l1, l2, l3 = plt.plot(t, S, t, I, t, R)
    fig.legend((l1, l2, l3), ('$S$', '$I$', '$R$'))
    plt.xlabel('часы')
    plt.show()

    
if __name__ == "__main__":
    demo_population_growth()
    demo_SIR()
