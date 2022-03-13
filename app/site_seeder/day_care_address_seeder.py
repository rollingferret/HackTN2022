"""Add geolocational data to day care JSON file.

Addresses deemed "inexact" are accurate to the city and zip code.
"""

import json
import socket

from geopy.geocoders import Nominatim
app = Nominatim(user_agent='day_care_finder')

socket.setdefaulttimeout(900)
day_cares = json.load(open('../../react-app/public/site_data/formatted_day_cares.json'))
main_day_care_dictionary = {}

try:
    for day_care_name in day_cares:
        day_care = day_cares[day_care_name]
        geo_addy = app.geocode(day_care['address'], timeout=10)
        location = geo_addy.raw if geo_addy else app.geocode(day_care['address'].split(', ')[1]).raw 
        day_care['coordinates'] = {'latitude': float(location['lat']), 'longitude': float(location['lon']), 'accuracy': 'exact' if geo_addy else 'inexact'}
        main_day_care_dictionary[day_care_name] = day_care
        print(f"Added geolocation data for: {day_care['name']}")

    with open('../../react-app/public/site_data/formatted_day_cares.json', 'w') as formatted_day_cares_file:
        json.dump(main_day_care_dictionary, formatted_day_cares_file, indent=4)
        print('File successfully written :D')
except Exception as e:
    with open('../../react-app/public/site_data/formatted_day_cares.json', 'w') as formatted_day_cares_file:
        json.dump(main_day_care_dictionary, formatted_day_cares_file, indent=4)
        print(f'File partially written, :O, the following error was encountered: {e}')