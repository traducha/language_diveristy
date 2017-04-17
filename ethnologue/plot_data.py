#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import simplejson as json
import pprint
import os
from population_data.read import get_population


translations = {
    'Surinam': 'Suriname',
    'Syria': 'Syrian Arab Republic',
    'Macedonia': 'TFYR Macedonia',
    'Palestinian West Bank and Gaza': 'State of Palestine',
    'Western Samoa': 'Samoa',
    'St. Pierre and Miquelon': 'Saint Pierre and Miquelon',
    'Sarawak': 'Malaysia',
    'Venezuela': 'Venezuela (Bolivarian Republic of)',
    'Kalimantan': 'Indonesia',
    'USA': 'United States of America',
    'Nusa Tenggara': 'Indonesia',
    'Taiwan': 'China',
    'Cape Verde Islands': 'Cabo Verde',
    'Moldova': 'Republic of Moldova',
    'Guinea Bissau': 'Guinea-Bissau',
    'Hong Kong': 'China, Hong Kong SAR',
    'Sabah': 'Malaysia',
    'Iran': 'Iran (Islamic Republic of)',
    'Brunei': 'Brunei Darussalam',
    'Sao Tome e Principe': 'Sao Tome and Principe',
    'U.S. Virgin Islands': 'United States Virgin Islands',
    'Bosnia-Herzegovina': 'Bosnia and Herzegovina',
    'St. Vincent and the Grenadines': 'Saint Vincent and the Grenadines',
    'Bali': 'Indonesia',
    'Russia': 'Russian Federation',
    'Irian Jaya': 'Papua New Guinea',
    'Azerbaijani': 'Azerbaijan',
    'St. Kitts-Nevis': 'Saint Kitts and Nevis',
    'Uzbekistan ': 'Uzbekistan',
    'Kyrghyzstan': 'Kyrgyzstan',
    'Comoros Islands': 'Comoros',
    'Laos': "Lao People's Democratic Republic",
    'Java': 'Indonesia',
    'USA (1 in Iowa': 'United States of America',
    'Norfolk Island': 'Australia',
    'Macau': 'China, Macao SAR',
    'Wallis and Futuna': 'Wallis and Futuna Islands',
    'Antigua': 'Antigua and Barbuda',
    'Tanzania': 'United Republic of Tanzania',
    "C&ocirc;te d'Ivoire": "C\xf4te d'Ivoire",
    'St. Lucia': 'Saint Lucia',
    'Mongolian Peoples Republic': 'Mongolia',
    'Maluku': 'Indonesia',
    'Bolivia': 'Bolivia (Plurinational State of)',
    'Sumatra': 'Indonesia',
    'Sulawesi': 'Indonesia',
    'Tahiti': 'French Polynesia',
    'Za&iuml;re': 'Democratic Republic of the Congo',
    'Korea, South': 'Republic of Korea',
    'Korea, North': "Dem. People's Republic of Korea",
}

population = get_population(1996)
# pprint.pprint(population)

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'languages.json')
with open(file_path, 'rb') as _file:
    languages = json.load(_file)
# pprint.pprint(languages)

check_l = 0
check_d = 0


def get_languages():
    count_lang = {}
    global check_l
    global check_d
    wrong_count = set()
    for lang, vals in languages.items():
        used = False
        for c in vals['countries']:
            if c in ['Asia', 'Europe']:
                continue
            country = translations.get(c) or c
            if country in count_lang:
                used = True
                count_lang[country]['langs'] += 1
                count_lang[country]['dials'] += 1 + len(vals['dialects'])
            else:
                try:
                    pop = population[country]
                except:
                    wrong_count.add(country)
                    continue
                used = True
                count_lang[country] = {
                    'langs': 1,
                    'dials': 1 + len(vals['dialects']),
                    'pop': pop
                }
        if used:
            check_l += 1
            check_d += 1 + len(vals['dialects'])

    print('No country: {}'.format(wrong_count))
    return count_lang


if __name__ == '__main__':
    dials_num = []
    langs_num = []
    langs_pop = []
    for country, vals in get_languages().items():
        langs_pop.append(vals['pop'])
        langs_num.append(vals['langs'])
        dials_num.append(vals['dials'])

    print 'Countries: {}'.format(len(langs_pop))
    print 'Languages: {}'.format(check_l)
    print 'Dialects: {}'.format(check_d)

    plt.scatter(langs_pop, langs_num, color='blue')
    plt.scatter(langs_pop, dials_num, color='green')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
