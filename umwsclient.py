# umwsclient.py --- web service client

# Copyright  (C)  2015  Marcelo Toledo <marcelo@marcelotoledo.com>

# Version: 1.0
# Keywords: 
# Author: Marcelo Toledo <marcelo@marcelotoledo.com>
# Maintainer: Marcelo Toledo <marcelo@marcelotoledo.com>
# URL: http://

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

import requests
import json

class UMWSClient:
    def __init__(self):
        self.server   = 'http://127.0.0.1:5000/api/v1.0'
        self.headers  = { 'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                          'Content-Type': 'application/json' }
        self.url      = None
        self.response = None

    def set_url(self, service):
        self.url = self.server + service

    def link_exist(self, link):
        self.set_url('/links/search/?q=' + link)
        self.response = requests.get(self.url, headers=self.headers)
        return self.response.status_code == 200
        
    def persist_link(self, link):
        self.set_url('/links/')
        data = { 'link': link }
        self.response = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        return self.response.status_code == 200
