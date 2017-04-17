#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import pprint
from matplotlib import pyplot as plt
import simplejson as json
import csv


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
        print(lang)
    # content = [x for x in content if 'alt' not in x]
    # pprint.pprint(content)
    return len(content)


if __name__ == '__main__':
    num = 0
    for l in letters:
        num += download_one_letter(l)
    print("languagaes {}".format(num))
