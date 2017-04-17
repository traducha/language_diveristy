#!/usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import simplejson as json
import csv
import os


country_codes = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'country_codes.csv')
data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'countries.json')
countries = {}

# https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population
with open(country_codes, 'rb') as _file:
    for name, code, code_a3, number, population in csv.reader(_file, delimiter=';', quotechar='|'):
        countries[code] = {
            'name': name,
            'population': population.replace(' ', '').replace(',', '')
        }

with open(data_file, 'r') as _file:
    data = json.load(_file)


continents = {
    'african': ['DZ', 'AO', 'SH', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CG', 'CD', 'DJ', 'EG', 'GQ',
                'ER', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'CI', 'KE', 'LS', 'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU',
                'YT', 'MA', 'MZ', 'NA', 'NE', 'NG', 'ST', 'RE', 'RW', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SH',
                'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'CD', 'ZM', 'TZ', 'ZW'],
    'asian': ['AF', 'AM', 'AZ', 'BH', 'BD', 'BT', 'BN', 'KH', 'CN', 'CX', 'CC', 'IO', 'GE', 'HK', 'IN', 'ID', 'IR',
              'IQ', 'IL', 'JP', 'JO', 'KZ', 'KW', 'KG', 'LA', 'LB', 'MO', 'MY', 'MV', 'MN', 'MM', 'NP', 'KP', 'OM',
              'PK', 'PS', 'PH', 'QA', 'SA', 'SG', 'KR', 'LK', 'SY', 'TW', 'TJ', 'TH', 'TR', 'TM', 'AE', 'UZ', 'VN',
              'YE'],
    'australian': ['AS', 'AU', 'NZ', 'CK', 'TL', 'FM', 'FJ', 'PF', 'GU', 'KI', 'MP', 'MH', 'UM', 'NR', 'NC', 'NZ', 'NU',
                   'NF', 'PW', 'PG', 'MP', 'WS', 'SB', 'TK', 'TO', 'TV', 'VU', 'UM', 'WF'],
    'european': ['AL', 'AD', 'AT', 'BY', 'BE', 'BA', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FO', 'FI', 'FR', 'DE', 'GI',
                 'GR', 'HU', 'IS', 'IE', 'IM', 'IT', 'RS', 'LV', 'LI', 'LT', 'LU', 'MK', 'MT', 'MD', 'MC', 'ME', 'NL',
                 'NO', 'PL', 'PT', 'RO', 'RU', 'SM', 'RS', 'SK', 'SI', 'ES', 'SE', 'CH', 'UA', 'GB', 'VA', 'RS'],
    'north_american': ['AI', 'AG', 'AW', 'BS', 'BB', 'BZ', 'BM', 'BQ', 'VG', 'CA', 'KY', 'CR', 'CU', 'CW', 'DM', 'DO',
                       'SV', 'GL', 'GD', 'GP', 'GT', 'HT', 'HN', 'JM', 'MQ', 'MX', 'PM', 'MS', 'CW', 'KN', 'NI', 'PA',
                       'PR', 'BQ', 'BQ', 'SX', 'KN', 'LC', 'PM', 'VC', 'TT', 'TC', 'US', 'VI'],
    'south_american': ['AR', 'BO', 'BR', 'CL', 'CO', 'EC', 'FK', 'GF', 'GY', 'GY', 'PY', 'PE', 'SR', 'UY', 'VE'],
}


def plot_all_in_one(aggr=False):
    fig = plt.figure()
    bins = 10.0

    for i, cont in enumerate(continents):
        ax = fig.add_subplot('32{}'.format(i + 1))
        pops = []
        aggr_pops = []
        langs = []
        aggr_langs = []
        excludes = []#['CN', 'IN']

        for code, lang_num in data.items():
            if int(lang_num) != 0 and countries[code]['population'] != '' and code in continents[cont] and code not in excludes:
                pops.append(int(countries[code]['population']))
                langs.append(int(lang_num))

        for j in range(int(bins)):
            from_ = min(pops) + j * (max(pops)+1.0 - min(pops)) / bins
            to = from_ + (max(pops)+1.0 - min(pops)) / bins
            aggr_pops.append((from_ + to) / 2.0)
            aggr_langs.append(0.0)
            num = 0.0
            for k, p in enumerate(pops):
                if from_ <= p < to:
                    aggr_langs[-1] += langs[k]
                    num += 1.0
            if num > 0.0:
                aggr_langs[-1] /= num

        print(cont, len(langs))

        if aggr:
            # ax.scatter(aggr_pops, aggr_langs)
            plt.bar(aggr_pops, aggr_langs, align='center', width=0.9 * (max(pops) + 1.0 - min(pops)) / bins)
        else:
            ax.scatter(pops, langs)
        # ax.set_xscale('log')
        # ax.set_yscale('log')
        ax.text(200000, 50, cont)
        if i + 1 == 3:
            ax.set_ylabel('Number of languages')
        if i + 1 in (5, 6):
            ax.set_xlabel('Size of the population')

    plt.tight_layout(h_pad=0.0, w_pad=0.1)
    plt.show()
    #plt.savefig('/home/tomaszraducha/Pulpit/languages.pdf', format='pdf')


def plot_all(aggr=False, cont=None):
    bins = 10.0
    pops = []
    aggr_pops = []
    langs = []
    aggr_langs = []
    excludes = ['CN', 'IN']

    for code, lang_num in data.items():
        if int(lang_num) != 0 and countries[code]['population'] != '' and code not in excludes and\
                ((cont is not None and code in continents[cont]) or cont is None):
            pops.append(int(countries[code]['population']))
            langs.append(int(lang_num))

    for j in range(int(bins)):
        from_ = min(pops) + j * (max(pops) + 1.0 - min(pops)) / bins
        to = from_ + (max(pops) + 1.0 - min(pops)) / bins
        aggr_pops.append((from_ + to) / 2.0)
        aggr_langs.append(0.0)
        num = 0.0
        for k, p in enumerate(pops):
            if from_ <= p < to:
                aggr_langs[-1] += langs[k]
                num += 1.0
        if num > 0.0:
            aggr_langs[-1] /= num

    print(len(langs))

    if aggr:
        # plt.scatter(aggr_pops, aggr_langs)
        plt.bar(aggr_pops, aggr_langs, align='center', width=0.9*(max(pops) + 1.0 - min(pops))/bins)
    else:
        plt.scatter(pops, langs)
    # ax.set_xscale('log')
    # ax.set_yscale('log')

    plt.ylabel('Number of languages')
    plt.xlabel('Size of the population')
    plt.tight_layout()
    plt.show()
    # plt.savefig('/home/tomaszraducha/Pulpit/languages_hist.pdf', format='pdf')


def get_languages():
    pops = []
    langs = []
    for code, lang_num in data.items():
        if int(lang_num) != 0 and countries[code]['population'] != '':
            pops.append(int(countries[code]['population']))
            langs.append(int(lang_num))
    return pops, langs


if __name__ == '__main__':
    # plot_all_in_one(aggr=True)
    plot_all(aggr=True, cont=None)
