#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
from ethnologue import plot_data
from wals import main
import sys
import matplotlib as mpl
mpl.rcParams['font.family'] = 'serif'

blue = '#21759B'
red = '#C40233'
green = '#4B6F44'

bins = 10.0  # 15
ticksize = 9 * 0.75 / 0.5
axsize = 12 * 0.75 / 0.5


wals_pops, wals_langs = main.get_languages()
wals_pops = [x/1.0 for x in wals_pops]

dials_eth = []
langs_eth = []
eth_pop = []
m = 0
lm = None
m2 = 0
lm2 = None
m3 = 0
lm3 = None
for country, vals in plot_data.get_languages().items():
    eth_pop.append(vals['pop']/1.0)
    if vals['langs'] > m:
        m = vals['langs']
        lm = country
    langs_eth.append(vals['langs'])
    dials_eth.append(vals['dials'])
for country, vals in plot_data.get_languages().items():
    if vals['langs'] > m2 and vals['langs'] != m:
        m2 = vals['langs']
        lm2 = country
for country, vals in plot_data.get_languages().items():
    if vals['langs'] > m3 and vals['langs'] not in (m, m2):
        m3 = vals['langs']
        lm3 = country
print lm, m
print lm2, m2
print lm3, m3
print sorted(eth_pop)[-4:]


plt.scatter(eth_pop, langs_eth, color=blue)
plt.scatter(eth_pop, dials_eth, color=green)
plt.scatter(wals_pops, wals_langs, color=red)
plt.xlim([1.0, 2000000])
plt.ylim([0.5, 10000])
plt.ylabel('Number of languages/dialects', fontsize=axsize)
plt.xlabel('Population [K]', fontsize=axsize)
plt.tick_params(axis='both', which='major', labelsize=ticksize)
plt.xscale('log')
plt.yscale('log')
plt.tight_layout()
# plt.show()
plt.savefig('/home/tomaszraducha/Pulpit/all_languages.pdf', transparent=True)
plt.savefig('/home/tomaszraducha/Pulpit/all_languages.eps', transparent=True)
plt.clf()



for i in xrange(2):
    # India 979 mln and China 1238 mln, third has 269 mln
    index_max = eth_pop.index(max(eth_pop))
    eth_pop.pop(index_max)
    langs_eth.pop(index_max)
    dials_eth.pop(index_max)

    index_max = wals_pops.index(max(wals_pops))
    wals_pops.pop(index_max)
    wals_langs.pop(index_max)

    # Indonesia 1196/3165 and Papua New Guinea 1082/2199, third is India /1271 or Nigeria 480/
    index_max = langs_eth.index(max(langs_eth))
    eth_pop.pop(index_max)
    langs_eth.pop(index_max)
    dials_eth.pop(index_max)


def aggregate(x, y):
    res_x = []
    res_y = []
    _min = min(x)
    _max = max(x)
    for j in range(int(bins)):
        from_ = _min + j * (_max + 1.0 - _min) / bins
        to = from_ + (_max + 1.0 - _min) / bins
        res_x.append((from_ + to) / 2.0)
        res_y.append(0.0)

        num = 0.0
        for k, p in enumerate(x):
            if from_ <= p < to:
                res_y[-1] += y[k]
                num += 1.0
        if num > 0.0:
            res_y[-1] /= num

    return res_x, res_y, 0.9*(_max + 1.0 - _min)/bins

# sys.exit(1)
wals_pops = [x/1000.0 for x in wals_pops]
eth_pop = [x/1000.0 for x in eth_pop]

wals_aggr_pops, wals_aggr_langs, ww = aggregate(wals_pops, wals_langs)
eth_aggr_pops, eth_aggr_langs, wl = aggregate(eth_pop, langs_eth)
eth_aggr_pops_d, eth_aggr_dials, wd = aggregate(eth_pop, dials_eth)

fig = plt.figure(figsize=[12, 4])
ax1 = fig.add_subplot('131')
ax1.bar(eth_aggr_pops, eth_aggr_langs, color=blue, align='center', width=wl)
ax1.set_ylabel('Number of languages/dialects', fontsize=axsize)
ax1.set_xlabel('Population [MM]', fontsize=axsize)
ax1.tick_params(axis='both', which='major', labelsize=ticksize)

ax2 = fig.add_subplot('132')
ax2.bar(eth_aggr_pops_d, eth_aggr_dials, color=green, align='center', width=wd)
ax2.set_xlabel('Population [MM]', fontsize=axsize)
ax2.tick_params(axis='both', which='major', labelsize=ticksize)

ax3 = fig.add_subplot('133')
ax3.bar(wals_aggr_pops, wals_aggr_langs, color=red, align='center', width=ww)
ax3.set_xlabel('Population [MM]', fontsize=axsize)
ax3.tick_params(axis='both', which='major', labelsize=ticksize)

plt.tight_layout()
# plt.show()
plt.savefig('/home/tomaszraducha/Pulpit/languages_hist.pdf', transparent=True)
plt.savefig('/home/tomaszraducha/Pulpit/languages_hist.eps', transparent=True)
plt.clf()
