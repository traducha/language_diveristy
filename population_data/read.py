#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import csv
import pprint


FILE_PATH = 'WPP2015_DB02_Populations_Annual.csv'


def get_population(year):
    countries = {}

    file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_PATH)
    with open(file_path, 'rb') as _file:
        data = iter(csv.reader(_file, delimiter=',', quotechar='|'))
        print 'columnws: ', next(data)

        for row in data:
            try:
                if int(row[4]) == year:
                    countries[row[1].replace('"', '')] = float(row[8])
            except:
                if row[1] + row[2] == '"China Hong Kong SAR"':
                    if int(row[5]) == year:
                        countries['China, Hong Kong SAR'] = float(row[9])
                elif row[1] + row[2] == '"China Macao SAR"':
                    if int(row[5]) == year:
                        countries['China, Macao SAR'] = float(row[9])
                elif 'developed regions' in row[1]:
                    continue
                else:
                    print row
                    raise
    return countries


if __name__ == '__main__':
    pprint.pprint(get_population(1996))
