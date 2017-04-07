#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import simplejson as json
import csv

country_codes = 'country_codes.csv'
countries = {}

# https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
with open(country_codes, 'rb') as _file:
    for name, code, code_a3, number, population in csv.reader(_file, delimiter=';', quotechar='|'):
        countries[code] = {
            'name': name,
            'population': population.replace(' ', '').replace(',', '')
        }

with open('countries.json', 'r') as _file:
    data = json.load(_file)


pops = []
langs = []

african = ['DZ', 'AO', 'SH', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CG', 'CD', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'CI', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'YT', 'MA', 'MZ', 'NA', 'NE', 'NG', 'ST', 'RE', 'RW', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SH', 'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'CD', 'ZM', 'TZ', 'ZW']
asian = ['AF', 'AM', 'AZ', 'BH', 'BD', 'BT', 'BN', 'KH', 'CN', 'CX', 'CC', 'IO', 'GE', 'HK', 'IN', 'ID', 'IR', 'IQ', 'IL', 'JP', 'JO', 'KZ', 'KW', 'KG', 'LA', 'LB', 'MO', 'MY', 'MV', 'MN', 'MM', 'NP', 'KP', 'OM', 'PK', 'PS', 'PH', 'QA', 'SA', 'SG', 'KR', 'LK', 'SY', 'TW', 'TJ', 'TH', 'TR', 'TM', 'AE', 'UZ', 'VN', 'YE']
australian = ['AS', 'AU', 'NZ', 'CK', 'TL', 'FM', 'FJ', 'PF', 'GU', 'KI', 'MP', 'MH', 'UM', 'NR', 'NC', 'NZ', 'NU', 'NF', 'PW', 'PG', 'MP', 'WS', 'SB', 'TK', 'TO', 'TV', 'VU', 'UM', 'WF']
european = ['AL', 'AD', 'AT', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FO', 'FI', 'FR', 'DE', 'GI', 'GR', 'HU', 'IS', 'IE', 'IM', 'IT', 'RS', 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC', 'ME', 'NL', 'NO', 'PL', 'PT', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'UA', 'GB', 'VA', 'RS']
north_american = ['AI', 'AG', 'AW', 'BS', 'BB', 'BZ', 'BM', 'BQ', 'VG', 'CA', 'KY', 'CR', 'CU', 'CW', 'DM', 'DO', 'SV', 'GL', 'GD', 'GP', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MX', 'PM', 'MS', 'CW', 'KN', 'NI', 'PA', 'PR', 'BQ', 'BQ', 'SX', 'KN', 'LC', 'PM', 'VC', 'TT', 'TC', 'US', 'VI']
south_american = ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'GY', 'PY', 'PE', 'SR', 'UY', 'VE']

for code, lang_num in data.items():
    if int(lang_num) != 0 and countries[code]['population'] != '' and code in south_american:
        pops.append(int(countries[code]['population']))
        langs.append(int(lang_num))

plt.scatter(pops, langs)
plt.show()
