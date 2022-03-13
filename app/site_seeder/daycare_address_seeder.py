"""Add geolocational info to daycare JSON file."""

"""Seed JSON file with longs and lats of daycare addresses."""

import json
from geopy.geocoders import Nominatim
app = Nominatim(user_agent='daycare_finder')

daycares = json.load(open('../../react-app/site_data/formatted_daycares.json'))
main_daycare_dictionary = {}

try:
    for daycare_name in daycares:
        daycare = daycares[daycare_name]
        geo_addy = app.geocode(daycare['address'], timeout=10)
        location = geo_addy.raw if geo_addy else app.geocode(daycare['address'].split()[2]).raw 
        daycare['coordinates'] = {'latitude': float(location['lat']), 'longitude': float(location['lon']), 'accuracy': 'exact' if geo_addy else 'inexact'}
        main_daycare_dictionary[daycare_name] = daycare
        print(f"Added geolocation data for: {daycare['name']}")

    with open('../../react-app/site_data/formatted_daycares.json', 'w') as formatted_daycares_file:
        json.dump(main_daycare_dictionary, formatted_daycares_file, indent=4)
        print('File successfully written :D')
except Exception as e:
    with open('../../react-app/site_data/formatted_daycares.json', 'w') as formatted_daycares_file:
        json.dump(main_daycare_dictionary, formatted_daycares_file, indent=4)
        print(f'File partially written, :O, the following error was encountered: {e}')