"""Seed JSON file with longs and lats of daycare addresses."""

import json
from geopy.geocoders import Nominatim
app = Nominatim(user_agent='daycare_finder')

daycares = json.load(open('../../react-app/site_data/daycare.json'))

main_daycare_dictionary = {}
for daycare in daycares:
    formatted_daycare = {}
    daycare_address = f'{daycare[2]}, {daycare[3]} {daycare[4]} {daycare[5]}'
    geo_address = app.geocode(daycare_address).raw if app.geocode(daycare_address) else app.geocode(daycare[3]).raw 
    formatted_daycare['coordinates'] = {'latitude': float(geo_address['lat']), 'longitude': float(geo_address['lon'])}
    main_daycare_dictionary[daycare[1]] = formatted_daycare

