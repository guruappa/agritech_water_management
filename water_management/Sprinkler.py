from abc import ABC, abstractmethod


class Sprinkler(ABC):
    def __init__(self, sprinkler_id, location, mqtt_client):
        self.sprinkler_id = sprinkler_id
        self.location = location
        self.mqtt_client = mqtt_client

    def start(self):
        pass

    def stop(self):
        pass

    def get_status(self):
        pass

    def subscribe_topic(self):
        pass

