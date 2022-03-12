"""Seed JSON file with structured daycare info."""

import json
from unittest import main
from geopy.geocoders import Nominatim
app = Nominatim(user_agent='daycare_finder')

daycares = json.load(open('../../react-app/site_data/daycare.json'))
# * MAKE SURE TO MAKE A CHECKBOX OR SOMETHING THAT SAYS WHETHER ADDRESS IS EXACT OR NOT
main_daycare_dictionary = {}
for i in range(len(daycares)):
    daycare = daycares[f'{i}']
    formatted_daycare = {}
    daycare_address = f'{daycare[2]}, {daycare[3]} {daycare[4]} {daycare[5]}'
    agent_contact_address = f'{daycare[8]}, {daycare[9]} {daycare[10]} {daycare[11]}'
    formatted_daycare['county'], formatted_daycare['name'], formatted_daycare['number'], formatted_daycare['agency_contact'] = daycare[0], daycare[1], daycare[6], daycare[7]
    formatted_daycare['address'] = daycare_address
    formatted_daycare['agency_contact_address'] = agent_contact_address
    formatted_daycare['minimum_age'] = daycare
    main_daycare_dictionary[daycare[1]] = formatted_daycare
    print(f'Added info for: {daycare[1]}')

with open('../../react-app/site_data/formatted_daycares.json', 'w') as formatted_daycares_file:
    json.dump(main_daycare_dictionary, formatted_daycares_file, indent=4)
    print('File successfully written :D')

"5": ["ANDERSON 0", "Weekday Early Education Wee Ministry 1", "225 North Main Street 2", "Clinton 3", "TN 4", "37716 5", "(865) 457-6685 6", "TAMMY BRADEN 7","PO Box 268 8", 
"Clinton 9",
 "TN 10", 
 "37717 11", 
 "16MO 12", "12YR 13", "2 14", "Center 15", "128 16", "07:00 AM 17", "05:30 PM 18", "N 19", "Y 20", "N 21", "Y 22", "Y 23", "N 24", "DHS Licensing 25", "Licensed 26", "11/1/2020 27", "1/1/1985 28", "N 29", "Y 30", "Y 31", "Y 32", "Y 33", "Y 34", "N 35", "DAVID CAPPS 36", "(865) 594-9138 37"],