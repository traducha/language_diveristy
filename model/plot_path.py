#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit as fit
import pickle
import pprint
import sys


ticksize = 14
axsize = 16

def lin(x, a, b):
    if isinstance(x, list):
        return [a * i + b for i in x]
    return a * x + b


with open('/home/tomaszraducha/Dropbox/DaneAxelrod/mgr/mgr/path/cluster_paths_q3_av48.data', 'rb') as _file:
    path = pickle.load(_file)

x, y = [], []
for k, v in path.items():
    if k < 4100:
        x.append(k)
        y.append(v)
popt, pcov = fit(lin, x, y)
print popt[0]
plt.plot(range(410, 4100, 2), lin(range(410, 4100, 2), popt[0], popt[1]), 'k-')
plt.scatter(x, y, marker='s', s=20*2, color='blue')

with open('/home/tomaszraducha/Dropbox/DaneAxelrod/mgr/mgr/path/high_k_cluster_paths_q3_av80.data', 'rb') as _file:
    path = pickle.load(_file)

x, y = [], []
for k, v in path.items():
    if k < 4100:
        x.append(k)
        y.append(v)
popt, pcov = fit(lin, x, y)
plt.plot(range(410, 4100, 2), lin(range(410, 4100, 2), popt[0], popt[1]), 'k-')
print popt[0]
plt.scatter(x, y, marker='s', s=20*2, color='orange')

plt.xlim([300, 4300])
plt.ylim([0, 26])
plt.xlabel('N', fontsize=axsize)
plt.ylabel('av. path length', fontsize=axsize)
plt.tick_params(axis='both', which='major', labelsize=ticksize)
plt.tight_layout()
plt.show()
# plt.savefig('/home/tomaszraducha/Pulpit/path.pdf')
# plt.savefig('/home/tomaszraducha/Pulpit/path.eps')
