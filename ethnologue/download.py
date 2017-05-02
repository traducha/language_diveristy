#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import pprint
import simplejson as json


RES_FILE = 'languages.json'
TIMEOUT = 5
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
}
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

languages = {}


def download_one_letter(letter):
    url_string = 'http://www.ethnologue.com/13/names/{}.html'.format(letter)
    print 'requesting {}'.format(url_string)

    try:
        req = urllib2.Request(url_string, headers=headers)
        content = urllib2.urlopen(req, timeout=TIMEOUT).read()
    except urllib2.HTTPError:
        raise
    content = content.split('<HR>')[0]
    content = content.split('</H1>')[-1]
    content = content.replace('<P>', '')
    content = content.replace('</P>', '')
    content = content.split('<BR>')

    for lang in content:
        lang = lang.replace('\r', '')
        lang = lang.replace('\n', '')

        if 'alt' in lang:
            continue
        elif len(lang) == 0:
            continue
        elif 'lang' in lang:
            lang_name = lang.split('[')[0][:-1]
            countries = lang.split(']')[1].replace(' lang, ', '').split(', ')

            if 'Korea' in countries:
                if countries[countries.index('Korea') + 1] in ['North', 'South']:
                    new_c = 'Korea, {}'.format(countries[countries.index('Korea') + 1])
                    countries.remove(countries[countries.index('Korea') + 1])
                    countries.remove('Korea')
                    countries.append(new_c)
            if 'Korea' in countries:  # the second Korea
                if countries[countries.index('Korea') + 1] in ['North', 'South']:
                    new_c = 'Korea, {}'.format(countries[countries.index('Korea') + 1])
                    countries.remove(countries[countries.index('Korea') + 1])
                    countries.remove('Korea')
                    countries.append(new_c)

            if lang_name in languages:
                languages[lang_name]['countries'].extend(countries)
            else:
                languages[lang_name] = {'countries': countries, 'dialects': []}
        elif 'dial' in lang:
            dial_name, lang_name = lang.split(' dial of ')
            lang_name = lang_name.split(' [')[0]
            if lang_name in languages:
                languages[lang_name]['dialects'].append(dial_name)
            else:
                languages[lang_name] = {'countries': [], 'dialects': [dial_name]}
        else:
            print 'WARNIG!', lang
            # raise BaseException


if __name__ == '__main__':
    for l in letters:
        download_one_letter(l)
    # pprint.pprint(languages)

    print("languagaes {}".format(len(languages.keys())))
    dials = []
    for lang, vals in languages.items():
        dials.extend(vals['dialects'])
    print("dialects {}".format(len(set(dials))))

    count = []
    for lang, vals in languages.items():
        if len(vals['countries']) != len(set(vals['countries'])):
            print 'WARNING!', lang, vals
            print len(vals['countries']), len(set(vals['countries']))
        count.extend(vals['countries'])
    print("countries {}".format(len(set(count))))

    with open(RES_FILE, 'w+') as _file:
        json.dump(languages, _file, indent=2)

    # 6866 languages
    # 9130 dialects
