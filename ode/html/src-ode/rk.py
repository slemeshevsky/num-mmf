# -*- coding: utf-8 -*-
import numpy as np

def RK4(F, u0, dt, t_end):
    N = int(t_end/dt)
    omega = np.linspace(0, N*dt, N)
    y = np.array(u0)
    sol = []
    sol.append(y)
    for t in omega:
        k1 = F(t, y)
        k2 = F(t + 0.5*dt, y + 0.5*dt*k1)
        k3 = F(t + 0.5*dt, y + 0.5*dt*k2)
        k4 = F(t + dt, y + dt*k3)

        y = y + dt/6*(k1 + 2*k2 + 2*k3 + k4)
        sol.append(y)

    return omega, y
