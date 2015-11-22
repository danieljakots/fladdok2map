#!/usr/bin/env python3.4

#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                   Version 2, December 2004

# Copyright (C) 2015 Daniel Jakots <vigdis@chown.me>

# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.

#           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

# 0. You just DO WHAT THE FUCK YOU WANT TO.
#

import requests
import json

def map_url(latitude, longitude):
    osm = 'https://www.openstreetmap.org/'
    level = 16
    map_url = '#map=' + str(level) + '/' + str(latitude) + '/' + str(longitude) + '/'
    pointer_url = '?mlat=' + str(latitude) +'&mlon=' + str(longitude)
    url = osm + pointer_url + map_url
    return(url)


def lookup(address):
    addok_url = 'http://api-adresse.data.gouv.fr/search/?q='
    r = requests.get(addok_url + address)
    # if the HTTP answer is not OK, abort
    if r.status_code == 200:
        address_book = []
        for f in r.json()['features']:
            pertinence = str(int(f['properties']['score'] * 100))
            text = (f['properties']['label'] + ' (Pertinence : ' + pertinence + '%)')
            latitude = f['geometry']['coordinates'][1]
            longitude = f['geometry']['coordinates'][0]
            url = map_url(latitude, longitude)
            address_book.append({text: url})

        return address_book

