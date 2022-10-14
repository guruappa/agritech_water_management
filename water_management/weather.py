from pyowm.owm import OWM
from water_management import utilities


def get_humidity():
    pass


def get_temperature():
    pass


def get_current_data(district, country):
    api_key = utilities.get_owm_key()
    owm = OWM(api_key)
    reg = owm.city_id_registry()
    loc = reg.locations_for(district, country=country)[0]

    mgr = owm.weather_manager()
    one_call = mgr.one_call(loc.lat, loc.lon)



def get_forecast_data(district, country):
    pass
