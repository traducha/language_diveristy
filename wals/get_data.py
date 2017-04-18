#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import simplejson as json
import csv


TIMEOUT = 3
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}

country_codes = 'codes.json'
countries = {}


with open(country_codes, 'rb') as _file:
    c_codes = json.load(_file)
for c_code in c_codes:
    countries[c_code['Code']] = 0


for code in countries.keys():
    url_string = 'http://wals.info/country/{}'.format(code)
    # print 'requesting {}'.format(url_string)

    try:
        req = urllib2.Request(url_string, headers=headers)
        url_content = urllib2.urlopen(req, timeout=TIMEOUT).read()
    except urllib2.HTTPError:
        print code
        continue

    for table in BeautifulSoup(url_content, 'lxml', parse_only=SoupStrainer('table')):
        if str(table) == 'html':
            continue
        # print(str(table).count('<tr>'))
        countries[code] = str(table).count('<tr>')


with open('countries.json', 'w+') as _file:
    json.dump(countries, _file, indent=2)
