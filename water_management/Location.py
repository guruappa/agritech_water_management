from abc import ABC, abstractmethod


class Location(ABC):
    def __init__(self, location_id, district, country):
        self.location_id = location_id
        self.district = district
        self.country = country

    def get_lat_long(self):
        pass

    def get_current_weather(self):
        pass

    def get_weather_forecast(self):
        pass
