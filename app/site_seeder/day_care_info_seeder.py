"""Seed JSON file with structured day care info."""

import json

day_cares = json.load(open('../../react-app/public/site_data/day_cares.json'))
main_day_care_dictionary = {}

for i in range(len(day_cares)):
    day_care = day_cares[f'{i}']
    formatted_day_care = {}
    day_care_address = f'{day_care[2]}, {day_care[3]} {day_care[4]} {day_care[5]}'
    agent_contact_address = f'{day_care[8]}, {day_care[9]} {day_care[10]} {day_care[11]}'
    formatted_day_care['county'], formatted_day_care['name'], formatted_day_care['number'], formatted_day_care['agency_contact'] = day_care[0], day_care[1].strip(), day_care[6], day_care[7]
    formatted_day_care['minimum_age'], formatted_day_care['maximum_age'], formatted_day_care['star_rating'], formatted_day_care['provider_type'] = day_care[12], day_care[13], f'{day_care[14]}/3', day_care[15]
    formatted_day_care['capacity'], formatted_day_care['open_time'], formatted_day_care['close_time'] = day_care[16], day_care[17], day_care[18]
    formatted_day_care['certificate_program_participant'] = True if day_care[19] == 'Y' else False
    formatted_day_care['offers_scholarship'] = True if day_care[20] == 'Y' else False
    formatted_day_care['offers_sliding_scale_fee'] = True if day_care[21] == 'Y' else False
    formatted_day_care['offers_multi_child_discount'] = True if day_care[22] == 'Y' else False
    formatted_day_care['approved_for_transportation'] = True if day_care[23] == 'Y' else False
    formatted_day_care['charges_fee_for_transportation'] = True if day_care[24] == 'Y' else False
    formatted_day_care['regulatory_agency'], formatted_day_care['regulatory_status'], formatted_day_care['license_approval_date'], formatted_day_care['establishment_date'] = day_care[25], day_care[26], day_care[27], day_care[28]
    formatted_day_care['near_public_transportation'] = True if day_care[29] == 'Y' else False
    formatted_day_care['wheel_chair_accessible'] = True if day_care[30] == 'Y' else False
    formatted_day_care['no_smoking'] = True if day_care[31] == 'Y' else False
    formatted_day_care['no_cats'] = True if day_care[32] == 'Y' else False
    formatted_day_care['no_pets'] = True if day_care[33] == 'Y' else False
    formatted_day_care['child_and_adult_care_food_program_participant'] = True if day_care[34] == 'Y' else False
    formatted_day_care['offers_scholarship'] = True if day_care[35] == 'Y' else False
    formatted_day_care['program_evaluator'] = day_care[36]
    formatted_day_care['program_evaluator_number'] = day_care[37]
    formatted_day_care['address'] = day_care_address
    formatted_day_care['agency_contact_address'] = agent_contact_address
    main_day_care_dictionary[day_care[1].strip()] = formatted_day_care
    print(f'Added info for: {day_care[1]}')

with open('../../react-app/public/site_data/formatted_day_cares.json', 'w') as formatted_day_cares_file:
    json.dump(main_day_care_dictionary, formatted_day_cares_file, indent=4)
    print('File successfully written :D')