"""Seed JSON file with longs and lats of daycare addresses."""

import json

daycares = json.load(open('../../react-app/site_data/daycare.json'))

print(daycares)