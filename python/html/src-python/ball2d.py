# -*- coding: utf-8 -*-

def y(v0y, t):
	g = 9.81
	return v0y*t - 0.5*g*t**2

def x(v0x, t):
	return v0x*t

initial_velocity_x = 2.0
initial_velocity_y = 5.0

time = 0.6
print x(initial_velocity_x, time), y(initial_velocity_x, time)
time = 0.9
print x(initial_velocity_x, time), y(initial_velocity_x, time)

# -*- 1st End

# Альтернативный вариант вычисления координат
def xy(v0x, v0y, t):
	g = 9.81
	return v0x*t, v0y*t - 0.5*g*t**2

# -*- 2d End

print xy(initial_velocity_x, initial_velocity_y, time)

# -*- 3d End
# Использование именованных аргументов

# -*- 4th Start
def xy_named(t, v0x = 0, v0y = 0):
	g = 9.81
	return v0x*t, v0y*t - 0.5*g*t**2

# -*- 4th End
# Использование строки документации

# -*- 5th Start
def xy_named(t, v0x = 0, v0y = 0):
	"""Вычисляются координаты x и y положения мяча в момент времени t """
	g = 9.81
	return v0x*t, v0y*t - 0.5*g*t**2
