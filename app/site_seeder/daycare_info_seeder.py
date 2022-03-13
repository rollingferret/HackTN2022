"""Seed JSON file with structured daycare info."""

import json

daycares = json.load(open('../../react-app/src/site_data/daycare.json'))
main_daycare_dictionary = {}

for i in range(len(daycares)):
    daycare = daycares[f'{i}']
    formatted_daycare = {}
    daycare_address = f'{daycare[2]}, {daycare[3]} {daycare[4]} {daycare[5]}'
    agent_contact_address = f'{daycare[8]}, {daycare[9]} {daycare[10]} {daycare[11]}'
    formatted_daycare['county'], formatted_daycare['name'], formatted_daycare['number'], formatted_daycare['agency_contact'] = daycare[0], daycare[1].strip(), daycare[6], daycare[7]
    formatted_daycare['minimum_age'], formatted_daycare['maximum_age'], formatted_daycare['star_rating'], formatted_daycare['provider_type'] = daycare[12], daycare[13], f'{daycare[14]}/3', daycare[15]
    formatted_daycare['capacity'], formatted_daycare['open_time'], formatted_daycare['close_time'] = daycare[16], daycare[17], daycare[18]
    formatted_daycare['certificate_program_participant'] = True if daycare[19] == 'Y' else False
    formatted_daycare['offers_scholarship'] = True if daycare[20] == 'Y' else False
    formatted_daycare['offers_sliding_scale_fee'] = True if daycare[21] == 'Y' else False
    formatted_daycare['offers_multi_child_discount'] = True if daycare[22] == 'Y' else False
    formatted_daycare['approved_for_transportation'] = True if daycare[23] == 'Y' else False
    formatted_daycare['charges_fee_for_transportation'] = True if daycare[24] == 'Y' else False
    formatted_daycare['regulatory_agency'], formatted_daycare['regulatory_status'], formatted_daycare['license_approval_date'], formatted_daycare['establishment_date'] = daycare[25], daycare[26], daycare[27], daycare[28]
    formatted_daycare['near_public_transportation'] = True if daycare[29] == 'Y' else False
    formatted_daycare['wheel_chair_accessible'] = True if daycare[30] == 'Y' else False
    formatted_daycare['no_smoking'] = True if daycare[31] == 'Y' else False
    formatted_daycare['no_cats'] = True if daycare[32] == 'Y' else False
    formatted_daycare['no_pets'] = True if daycare[33] == 'Y' else False
    formatted_daycare['child_and_adult_care_food_program_participant'] = True if daycare[34] == 'Y' else False
    formatted_daycare['offers_scholarship'] = True if daycare[35] == 'Y' else False
    formatted_daycare['program_evaluator'] = daycare[36]
    formatted_daycare['program_evaluator_number'] = daycare[37]
    formatted_daycare['address'] = daycare_address
    formatted_daycare['agency_contact_address'] = agent_contact_address
    main_daycare_dictionary[daycare[1].strip()] = formatted_daycare
    print(f'Added info for: {daycare[1]}')

with open('../../react-app/src/site_data/formatted_daycares.json', 'w') as formatted_daycares_file:
    json.dump(main_daycare_dictionary, formatted_daycares_file, indent=4)
    print('File successfully written :D')