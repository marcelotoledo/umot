#!/usr/local/bin/python3
#
# umot.py --- url monitor

# Copyright  (C)  2015  Marcelo Toledo <marcelo@marcelotoledo.com>

# Version: 1.0
# Keywords:
# Author: Marcelo Toledo <marcelo@marcelotoledo.com>
# Maintainer: Marcelo Toledo <marcelo@marcelotoledo.com>
# URL: http://marcelotoledo.com

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

# Commentary:


# Code:

import sys
import requests
from bs4 import BeautifulSoup

version = "0.1"

def valid_href(link):
    href = link.get('href')
    if href and len(href):
        return True
    return False


def get_links(response):
    soup = BeautifulSoup(response)
    hrefs = [a.get('href') for a in soup.findAll('a')
             if a.get('href') and len(a.get('href')) > 1]
    return list(set(hrefs))


def get_url(url):
    headers = {
        'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
    return requests.get(url, headers=headers)

def check_broken_link(url):
    response = get_url(url)
    return response.status_code is not 200

def usage():
    print("Usage: %s [url]" % sys.argv[0])


def main():
    print("umot ver %s - Copyright 2014 (C) Marcelo Toledo\n" % version)

    if len(sys.argv) != 2:
        usage()
        return

    print("Scanning url %s..." % sys.argv[1])

    url = sys.argv[1]
    response = get_url(url)
    links = get_links(response.text)

    internal_links = filter(lambda x: url in x, links)
    external_links = list(set(internal_links) - set(links))

    broken_internal = filter(lambda url: check_broken_link(url), internal_links)
    broken_external = filter(lambda url: check_broken_link(url), external_links)


    print 'Amount of internal URLs: %s' % len(internal_links)
    if len(broken_internal) > 0 :
        print 'List of broken internal URLs:'
        for link in broken_internal:
            print '- %s' % link
    else:
        print 'There is not any broken internal URLs'

    print 'Amount of external URLs: %s' % len(external_links) 
    if len(broken_external) > 0 :
        print 'List of broken external URLs:'
        for link in broken_external:
            print '- %s' % link
    else:
        print 'There is not any broken external URLs'


if __name__ == '__main__':
    main()
