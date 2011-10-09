#!/usr/bin/python

# 1. add proxy support
# 2. specify results range
#       file should look like "kw startpage endpage file"
# 3. threads

import urllib
import urllib2
import re

regex = re.compile(r"<div class=\"s\">(.*?)<br><cite>")

def load_proxies(file):


def remove_tags(string):
        notags = re.compile(r"<[^<]*?>")
        return notags.sub('', string)

def scrape(kw):
        url = 'http://www.google.com/search?hl=en&q=' + kw + '&btnG=Google+Search&aq=f&oq='
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        data = None
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        the_list = regex.findall(the_page)
        return the_list

f = open('keywords.txt', 'r')
while 1:
        line = f.readline()
        if not line: break
        line = line.replace('\n', '')
        f2 = open(line + '.txt', 'w')
        lines = scrape(line)
        clean = []
        for e in lines:
                clean.append(remove_tags(e))
        f2.writelines(clean)
        f2.close()
f.close()


