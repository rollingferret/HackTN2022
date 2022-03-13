"""Add geolocational data to daycare JSON file."""

import json
from geopy.geocoders import Nominatim
app = Nominatim(user_agent='daycare_finder')

daycares = json.load(open('../../react-app/src/site_data/formatted_daycares_test.json'))
main_daycare_dictionary = {}

#try:
for daycare_name in daycares:
    daycare = daycares[daycare_name]

    try:
        geo_addy = app.geocode(daycare['address'], timeout=10)
        location = geo_addy.raw if geo_addy else app.geocode(daycare['address'].split()[2]).raw
    except Exception as e:
        continue
    daycare['coordinates'] = {'latitude': float(location['lat']), 'longitude': float(location['lon']), 'accuracy': 'exact' if geo_addy else 'inexact'}
    main_daycare_dictionary[daycare_name] = daycare
    print(f"Added geolocation data for: {daycare['name']}")

with open('../../react-app/src/site_data/formatted_daycares_test.json', 'w') as formatted_daycares_file:
    json.dump(main_daycare_dictionary, formatted_daycares_file, indent=4)
    print('File successfully written :D')
#except Exception as e:
    #with open('../../react-app/src/site_data/formatted_daycares_test.json', 'w') as formatted_daycares_file:
        #json.dump(main_daycare_dictionary, formatted_daycares_file, indent=4)
        #print(f'File partially written, :O, the following error was encountered: {e}')