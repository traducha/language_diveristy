#!/usr/bin/python
# -*- coding: utf-8 -*-
import simplejson as json
import pprint


file_path = 'WALS_data/africa.json'
countries = {}

with open(file_path, 'rb') as _file:
    data = json.load(_file)

pprint.pprint(data)
