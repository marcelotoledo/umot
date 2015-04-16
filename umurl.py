# umurl.py --- url manipulation

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

from bs4 import BeautifulSoup
import requests

class UMURL:
    def __init__(self, url):
        self.url         = url
        self.website     = None
        self.response    = None
        self.status_code = None
        self.content     = None
        self.links       = None

    def request(self):
        headers = {
            'User-agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}
        self.response    = requests.get(self.url, headers=headers)
        self.status_code = self.response.status_code
        self.content     = self.response.text

    def is_internal(self, url):
        # import re
        # match = '^' + self.website.replace('.', '\.')
        # if re.match(match, url) is None:
        #     return False
        # return True
        import re
        match = '^http://marcelotoledo\.com.*'
        if re.match(match, url) is None:
            return False
        return True

    def extract_ahrefs(self):
        soup = BeautifulSoup(self.content)
        hrefs = [a.get('href') for a in soup.findAll('a')
                 if a.get('href') and len(a.get('href')) > 1]
        self.links = list(set(hrefs))
        self.links = filter(self.is_internal, self.links)
