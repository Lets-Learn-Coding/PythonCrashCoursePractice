from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    #return 2 digit code
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    #If the country isnt found return none
    return None