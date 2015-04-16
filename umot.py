#!/usr/bin/env python
#
# umot.py ---

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
import ummq
import umurl
from umwsclient import UMWSClient

version = "0.1"

def callback(ch, method, properties, body):
    print(" [*] processing %s" % body)

    c = UMWSClient()
    
    if c.link_exist(body):
        print(" [!] NOT processing %s" % body)
        mq.ack(method)
        return False

    c.persist_link(body)

    url = umurl.UMURL(body)
    url.request()
    url.extract_ahrefs()

    url.website = 'http://marcelotoledo.com'
    #internal_links  = filter(lambda x: url.website in x, url.links)
    #internal_links  = filter(url.is_internal, url.links)
    
    #external_links = filter(lambda x: 'http://' in x, set(links) - set(internal_links))
    #external_links = remove_existent_links(external_links)

    for i in url.links:
        print(" [*] Queueing %s" % i)
        mq.write(i)

    mq.ack(method)

if __name__ == '__main__':
    print("umot ver %s - Copyright 2014 (C) Marcelo Toledo\n" % version)

    mq = ummq.UMMQueue('localhost', 'umot_queue', callback)

    mq.open()
    print(' [*] Waiting for the next item in queue')
    mq.consume()
