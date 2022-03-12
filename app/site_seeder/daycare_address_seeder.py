"""Add geolocational info to daycare JSON file."""

"""Seed JSON file with longs and lats of daycare addresses."""

import json
from geopy.geocoders import Nominatim
app = Nominatim(user_agent='daycare_finder')
# * MAKE SURE TO MAKE A CHECKBOX OR SOMETHING THAT SAYS WHETHER ADDRESS IS EXACT OR NOT

daycares = json.load(open('../../react-app/site_data/formatted_daycares.json'))

main_daycare_dictionary = {}
for i in range(len(daycares)):
    daycare = daycares[f'{i}']
    daycare_address = f'{daycare[2]}, {daycare[3]} {daycare[4]} {daycare[5]}'
    geo_addy = app.geocode(daycare_address, timeout=10)
    location = geo_addy.raw if geo_addy else app.geocode(daycare[3]).raw 
    coordinates = {'latitude': float(location['lat']), 'longitude': float(location['lon'])}
    main_daycare_dictionary[daycare[1]]['coordinates'] = coordinates
    print(f'Added geolocation data for: {daycare[1]}')

with open('../../react-app/site_data/formatted_daycares.json', 'w') as formatted_daycares_file:
    json.dump(main_daycare_dictionary, formatted_daycares_file, indent=4)
    print('File successfully written :D')