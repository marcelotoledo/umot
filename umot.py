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

version = "0.1"

def usage():
    print("Usage: %s [url]" % sys.argv[0])

def main():
    print("umot ver %s - Copyright 2014 (C) Marcelo Toledo\n" % version)
    
    if len(sys.argv) != 2:
        usage()
        return

    print("Scanning url %s..." % sys.argv[1])    
    

if __name__ == '__main__':
    main()
