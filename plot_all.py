#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import simplejson as json
import pprint
from ethnologue import plot_data
from wals import main


wals_pops, wals_langs = main.get_languages()
wals_pops = [x/1000.0 for x in wals_pops]

dials_eth = []
langs_eth = []
eth_pop = []
for country, vals in plot_data.get_languages().items():
    eth_pop.append(vals['pop'])
    langs_eth.append(vals['langs'])
    dials_eth.append(vals['dials'])


plt.scatter(eth_pop, langs_eth, color='blue')
plt.scatter(eth_pop, dials_eth, color='green')
plt.scatter(wals_pops, wals_langs, color='red')
plt.xscale('log')
plt.yscale('log')
plt.show()
