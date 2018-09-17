# -*- coding: utf-8 -*-

filename = 'data.txt'
import numpy as np
data = np.loadtxt(filename, comments="#")
x = data[:,0]
y = data[:,1]
data[:,1] = np.log(y)
filename = 'tmp.txt'
outfile = open(filename, 'w')
outfile.write('# координаты x и y\n')
np.savetxt(outfile, data, fmt='%10.5f')
