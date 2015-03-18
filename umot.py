#!/usr/bin/env python
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
import ummq
import umurl
import time
import psycopg2

version = "0.1"

def persist_links(links, is_internal = True):
    conn = psycopg2.connect("dbname=umot user=umot password=RabrXfC9ggBhyFWBsWAWoH3")
    cur  = conn.cursor()

    for i in links:
        internal = 'Y' if is_internal else 'N'
        print(" [*] Persisting %s into the database" % i)
        cur.execute("INSERT INTO link (id_website, link, internal) VALUES (1, %s, %s)", (i, internal))

    conn.commit()
    
    cur.close()
    conn.close()

def add_to_queue(links, mq):
    for i in links:
        print(" [*] Adding %s to the queue" % i)
        mq.write(i)

def remove_existent_links(links):
    conn = psycopg2.connect("dbname=umot user=umot password=RabrXfC9ggBhyFWBsWAWoH3")
    cur  = conn.cursor()

    for i in links:
        cur.execute("SELECT count(*) FROM link WHERE link=%s;", (i, ))
        res = cur.fetchone()
        if int(res[0]) > 0:
            print(" [*] Duplicated %s" % i)
            links.remove(i)

    cur.close()
    conn.close()

    return links
        

def callback(ch, method, properties, body):
    print(" [*] processing %s" % body)
    
    url = umurl.UMURL(body)
    url.request()
    url.extract_ahrefs()

    internal_links  = filter(lambda x: body in x, url.links)
    #external_links  = filter(lambda x: 'http://' in x, set(links) - set(internal_links))

    internal_links = remove_existent_links(internal_links)
    #external_links = remove_existent_links(external_links)

    add_to_queue(internal_links, mq)
    #add_to_queue(external_links)
    persist_links(internal_links)
    #persist_links(external_links, False)

    mq.ack(method)

if __name__ == '__main__':
    print("umot ver %s - Copyright 2014 (C) Marcelo Toledo\n" % version)

    mq = ummq.UMMQueue('localhost', 'umot_queue', callback)

    mq.open()
    print(' [*] Waiting for the next item in queue')
    mq.consume()
