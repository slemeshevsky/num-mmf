# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import time
    
def solver_Ex_simple(I, a, f, L, tau, F, T):
    """
    Простейшая реализация явной разностной схемы для приближенного решения
    параболического уравнения.
    """
    cpu = 0  # Для подсчета процессорного времени

    Nt = int(round(T/float(tau)))
    t = np.linspace(0, Nt*tau, Nt+1)  # сетка по времени
    h = np.sqrt(a*tau/F)
    Nx = int(round(L/float(h)))
    x = np.linspace(0, L, Nx+1)    # сетка по пространству

    # Для уверенности шаги по пространству и времени согласуем с сетками
    h = x[1] - x[0]
    tau = t[1] - t[0]

    u = np.zeros(Nx+1)
    u_n = np.zeros(Nx+1)

    # устанавливаем начальные условия u(x,0) = I(x)
    for i in range(0, Nx+1):
        u_n[i] = I(x[i])

    for n in range(1, Nt):
        # Вычисляем приближенное решение во внутренних узлах сетки
        for i in range(1, Nx):
            u[i] = u_n[i] + F*(u_n[i+1] - 2*u_n[i] + u_n[i-1]) + tau*f(x[i], t[n])

        # Задаем граничные условия
        u[0] = 0
        u[Nx] = 0

        # Обновляем переменные перед следующим шагом
        u_n, u = u, u_n

    cpu = time.perf_counter()
    return u, x, t, cpu
# End solver_Ex_simple

# Start solver_Ex
def solver_Ex(I, a, f, L, tau, F, T, user_action=None, version='scalar'):
    """
    Векторизованная реализация явной схемы
    """
    cpu = 0  # Для подсчета процессорного времени

    Nt = int(round(T/float(tau)))
    t = np.linspace(0, Nt*tau, Nt+1)  # сетка по времени
    h = np.sqrt(a*tau/F)
    Nx = int(round(L/float(h)))
    x = np.linspace(0, Nx*h, Nx+1)    # сетка по пространству

    # Для уверенности шаги по пространству и времени согласуем с сетками
    h = x[1] - x[0]
    tau = t[1] - t[0]

    u = np.zeros(Nx+1)
    u_n = np.zeros(Nx+1)

    # устанавливаем начальные условия u(x,0) = I(x)
    for i in range(0, Nx+1):
        u_n[i] = I(x[i])

    for n in range(0, Nt+1):
        # Вычисляем приближенное решение во внутренних узлах сетки
        if version == 'scalar':
            for i in range(1, Nx):
                u[i] = u_n[i] + F*(u_n[i+1] - 2*u_n[i] + u_n[i-1]) + tau*f(x[i], t[n])
        elif version == 'vectorized':
            u[1:Nx] = u_n[1:Nx] + F*(u_n[2:Nx+1] - 2*u_n[1:Nx] + u_n[0:Nx-1]) + tau*f(x[1:Nx], t[n])
        else:
            raise ValueError('version = {}'.format(version))

        # Задаем граничные условия
        u[0] = 0
        u[Nx] = 0

        if user_action is not None:
            user_action(u, x, t, n)

        # Обновляем переменные перед следующим шагом
        u_n, u = u, u_n

    cpu = time.perf_counter()
    return u, x, t, cpu
# End solver_Ex
# Start plug
def plug(scheme='Ex', F=0.5, Nx=50):
    L = 1.
    a = 1.
    T = 0.1
    # Вычисляем tau по Nx и F
    h = L/Nx
    tau = F*h**2/a

    def I(x):
        if abs(x - L/2) > 0.1:
            return 0.
        else:
            return 1.

    def f(x, t):
        return 0.0
   
    cpu = viz(I, a, f, L, tau, F, T,
              u_min=-0.1, u_max=1.1,
              scheme=scheme, animate=True,
              framefiles=True)
    print('Время расчета: {}'.format(cpu))
# End plug
# Start gaussian
def gaussian(scheme='Ex', F=0.5, Nx=50, sigma=0.05):
    L = 1.
    a = 1.
    T = 0.01
    # Вычисляем tau по Nx и F
    h = L/Nx
    tau = F*h**2/a

    def I(x):
        return np.exp(-0.5*((x - L/2)**2)/(sigma**2))

    def f(x, t):
        return np.zeros_like(x)

    cpu = viz(I, a, f, L, tau, F, T,
              u_min=-0.1, u_max=1.1,
              scheme=scheme, animate=True,
              framefiles=True)
    print('Время расчета: {}'.format(cpu))
# End gaussian
# Start viz
def viz(I, a, f, L, tau, F, T, u_min, u_max,
        scheme='Ex', animate=True, framefiles=True):
    def plot_u(u, x, t, n):
        plt.clf()
        plt.plot(x, u, 'r-')
        plt.axis([0., L, u_min, u_max])
        plt.title('$t=${}'.format(t[n]))
        if framefiles:
            plt.savefig('tmp_frame{:04d}.png'.format(n))
            plt.close()
            
    user_action = plot_u if animate else lambda u, x, t, n: None
    u, x, t, cpu = eval('solver_'+scheme)(I, a, f, L, tau, F, T,
                                          user_action=user_action)
    return cpu
# End viz
