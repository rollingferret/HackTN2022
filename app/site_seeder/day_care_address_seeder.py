"""Add geolocational data to day care JSON file.

If geocode can't pick up on the coordinates of an entire address, the 
program deems the coordinates "inexact" and uses state, city, and ZIP
to find coordinates. If the address is still not recognized, then the
program uses solely the ZIP. The accuracy of the inexact coordinates 
is then indicated beside the inexact status.
"""

import re
import json
from geopy.geocoders import Nominatim

app = Nominatim(user_agent='day_care_finder')
day_cares = json.load(open('../../react-app/public/site_data/formatted_day_cares.json'))
main_day_care_dictionary = {}

try:
    for day_care_name in day_cares:
        day_care = day_cares[day_care_name]
        geo_addy = app.geocode(day_care['address'], timeout=10)
        location, accuracy = None, None
        if geo_addy: location, accuracy = geo_addy.raw, 'exact'
        if not geo_addy:
            geo_addy_alt =  app.geocode(day_care['address'].split(', ')[1], timeout=10)
            if geo_addy_alt: location, accuracy = geo_addy_alt.raw, 'inexact (only accurate to the state, city, and ZIP)'
            else: 
                zip_code = re.match(r'(.*\s)([0-9]{1,}$)', day_care['address']).group(2)
                location, accuracy = app.geocode(zip_code, timeout=10).raw, 'inexact (only accurate to the ZIP)'
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