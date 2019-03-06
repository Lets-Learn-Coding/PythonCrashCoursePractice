import json
from pygal.maps.world import COUNTRIES
from pygal.maps.world import World
from country_code import get_country_code

#load the data
filename = 'gdp_json.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    country_name = pop_dict['Country Name']
    gdp = float(pop_dict['Value'])
    code = get_country_code(country_name)
    if pop_dict['Year'] == 2016 and code:
        cc_populations[code] = gdp
        print(str(code) + ": " + str(gdp))

wm = World()
wm.title = "World GDP 2016 by Country"
wm.add('2016', cc_populations)
wm.render_to_file('World_GDP.svg')
