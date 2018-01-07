#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit as fit
import pickle
import pprint
import sys
import glob
import re
import time
import logging as log
import numpy as np
import matplotlib as mpl
mpl.rcParams['font.family'] = 'sans-serif'


# q_list = [2, 5, 50, 100]
N_list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
styles = {2: 's', 5: 'o', 50: 'D', 100: '^'}

ticksize = 9 #* 0.75 / 0.5
axsize = 12 #* 0.75 / 0.5


def fetch_results():
    res = {}
    pattern = re.compile(r'([a-zA-Z2_]*)_domains_number_N([0-9]{1,4})_q([0-9]{1,4})_av[0-9]{1,4}\.data')
    for _file in glob.glob("/home/tomaszraducha/Dropbox/DaneAxelrod/mgr/mgr/domains_numbers/data/*.data"):
        match = pattern.match(_file.split('/')[-1])
        mode, N, q = match.groups()
        N = int(N)

        key = ''.join([mode, '_q=', q])
        if key not in res:
            res[key] = {}

        with open(_file, 'rb') as _f:
            results = pickle.load(_f)
        res[key][N] = {
            'dom_av': results['dom_av'],
            'dom_std': results['dom_std'],
            'com_av': results['com_av'],
            'com_std': results['com_std'],
        }
    return res


def plot_results(res, qs, ymin=0, name=None):
    a_, b_, c_ = None, None, None
    A = res.keys()
    A = sorted(A)
    for q_mode in A:
        results = res[q_mode]
        print q_mode
        q = int(q_mode.split('=')[-1])
        if q not in qs:
            continue
        dom_av = []
        dom_std = []
        com_av = []
        com_std = []
        n_list = []
        for N, values in results.items():
            dom_av.append(values['dom_av'])
            dom_std.append(values['dom_std'])
            com_av.append(values['com_av'])
            com_std.append(values['com_std'])
            n_list.append(N)

        if 'high_k_cluster' in q_mode:
            a = ax.scatter(n_list, com_av, color='#21759B', marker=styles[q], s=24*2)
            if a_ is None:
                a_ = True
                a.set_label('local rewiring 2')
        elif 'cluster' in q_mode:
            b = ax.scatter(n_list, com_av, color='#C40233', marker=styles[q], s=24*2)
            if b_ is None:
                b_ = True
                b.set_label('local rewiring 1')
        elif 'normal' in q_mode:
            c = ax.scatter(n_list, com_av, color='#EE7F2D', marker=styles[q], s=24*2)
            if c_ is None:
                c_ = True
                c.set_label('uniform rewiring')

    # handles, labels = ax.get_legend_handles_labels()
    # ax.legend(loc=2, fontsize=axsize, framealpha=0.0)
    # blue 3591d0
    # yellow ffd24d
    # red f3363e
    # purple d5a6f2
    # orange ffa517
    # green 96c824
    ax.set_xlabel('N', fontsize=axsize)
    ax.set_ylabel('Number of domains', fontsize=axsize)
    ax.set_xlim([50, 1050])
    ax.set_ylim(ymin=ymin)
    ax.tick_params(axis='both', which='major', labelsize=ticksize)


if __name__ == '__main__':
    res = fetch_results()
    # pprint.pprint(res)
    fig = plt.figure(figsize=[10, 4])
    ax = fig.add_subplot(121)
    plot_results(res, [50, 100], ymin=-50, name='models_q50_100')
    ax = fig.add_subplot(122)
    plot_results(res, [2, 5], ymin=-10, name='models_q2_5')
    plt.tight_layout()

    # plt.show()
    # plt.savefig('/home/tomaszraducha/Pulpit/{}.pdf'.format(name), transparent=True)
    plt.savefig('/home/tomaszraducha/Pulpit/{}.eps'.format('domains'), transparent=True, dpi=600)
    plt.clf()
