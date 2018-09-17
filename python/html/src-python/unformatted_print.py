# -*- coding: utf-8 -*-

from math import sin

t = 0
dt = 0.55

t += dt; f = t*sin(t)
print t, f

t += dt; f = t*sin(t)
print t, f

t += dt; f = t*sin(t)
print t, f


