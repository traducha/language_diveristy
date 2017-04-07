#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv


file_path = 'WALS_data/africa.csv'
countries = {}

with open(file_path, 'rb') as _file:
    data = iter(csv.reader(_file, delimiter=',', quotechar='|'))
    print next(data)

    for row in data:
        print row[2], row[10]
        if row[2] in countries:
            countries[row[2]] += 1
        else:
            countries[row[2]] = 1

print countries

