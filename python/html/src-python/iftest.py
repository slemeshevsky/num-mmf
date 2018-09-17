# -*- coding: utf-8 -*-

import random

x = 0.0; y = 0.0; d = 0.1

r = random.random()
if 0 <= r < 0.25:
	# перемещаемся на север
	y = y + d
elif 0.25 <= r < 0.5:
	# перемещаемся на восток
	x = x + d
elif 0.5 <= r < 0.75:
	# перемещаемся на юг
	y = y - d
else:
	# перемещаемся на запад
	x = x - d

print x, y
