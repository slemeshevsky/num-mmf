# -*- coding: utf-8 -*-

filename = 'data.txt'
infile = open(filename, 'r')   # открытие файла для чтения
line = infile.readline()       # чтение первой строки

# Чтение x и y из файла и сохранение их в списки
x = []; y = []
for line in infile:
	words = line.split()       # разбиение строки на слова
	x.append(float(words[0]))
	y.append(float(words[1]))
infile.close()

# Преобразование координаты y
from math import log

def f(y):
	return log(y)

for i in range(len(y)):
	y[i] = f(y[i])

# Запись x и y в файл из двух колонок
filename = 'tmp.txt'
outfile = open(filename, 'w')   # открытие файла для записи
outfile.write('# координаты x и y\n')
for xi, yi in zip(x, y):
	outfile.write('%10.5f %10.5f\n' % (xi, yi))
outfile.close()
