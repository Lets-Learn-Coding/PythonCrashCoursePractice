import json
import csv
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
from country_code import get_country_code
import pygal
from c_code import get_country_code


filename = 'urban_pop.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    cc_pop = {}
    for row in reader:
        try:
            country = (row[0])
            code = get_country_code(country)
            pop = float(row[11])
        except ValueError:
            print('unavailable')
        else:
            cc_pop[code] = int(float(pop))

wm = World()
wm.title = "World urban pop by Country"
wm.add('Urban', cc_pop)

wm.render_to_file('urban_population.svg')