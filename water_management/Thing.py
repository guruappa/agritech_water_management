from abc import ABC, abstractmethod
from AWSIoTPythonSDK.exception.AWSIoTExceptions import publishTimeoutException
from AWSIoTPythonSDK.core.protocol.internal.defaults import DEFAULT_OPERATION_TIMEOUT_SEC
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
import datetime
import json
import random

from water_management import utilities


class Thing(ABC):
    def __init__(self, thing_id, thing_parent, location, end_point, cert_filepath, private_key_file, ca_filepath):
        self.thing_id = thing_id
        self.thing_parent = thing_parent
        self.location = location
        self.end_point = end_point
        self.cert_filepath = cert_filepath
        self.private_key_file = private_key_file
        self.ca_filepath = ca_filepath

        # AWS MQTT Client
        self.mqtt_client = AWSIoTPyMQTT.AWSIoTMQTTClient(self.thing_id)
        self.mqtt_client.configureEndpoint(self.end_point, 8883)
        self.mqtt_client.configureCredentials(self.ca_filepath, self.private_key_file, self.cert_filepath)

        self._data = {"thing_id": self.thing_id, "thing_parent": self.thing_parent, "location": self.location}
        self._status = None

    @abstractmethod
    def _get_status(self):
        pass

    @abstractmethod
    def _set_status(self, status):
        pass

    @abstractmethod
    def _publish_data(self):
        pass

    @abstractmethod
    def _publish_heartbeat(self):
        pass

    def _send_message(self, topic):
        message_json = json.dumps(self._data)
        self.mqtt_client.connect()
        self.mqtt_client.publish(topic, message_json, 1)
        self.mqtt_client.disconnect()

    @abstractmethod
    def _subscribe_data(self):
        pass


class Sensor(Thing):
    def __init__(self, sensor_id, sprinkler, location, end_point, cert_filepath, private_key_file, ca_filepath):
        super().__init__(sensor_id, sprinkler, location, end_point, cert_filepath, private_key_file, ca_filepath)

    def _get_status(self):
        pass

    def _set_status(self, status):
        pass

    def _publish_heartbeat(self):
        heartbeat_topic = utilities.get_topic(self.location, self.thing_parent, self.thing_id, "heartbeat")
        self._data['heartbeat'] = True
        self._send_message(heartbeat_topic)

    def _publish_data(self):
        publish_topic = utilities.get_topic(self.location, self.thing_parent, self.thing_id, "publish")

        temp, humidity = self.get_value(dummy=True)
        self._data['timestamp'] = str(datetime.datetime.now())
        self._data['temperature'] = temp
        self._data['humidity'] = humidity

        self._send_message(publish_topic)

    # Dummy value
    def get_dummy_value(self):
        temp_value = round(float(random.normalvariate(15, 45)), 2)
        humidity_value = round(float(random.normalvariate(40, 90)), 2)
        return temp_value, humidity_value

    # Real value
    def get_value(self, dummy=False):
        if dummy:
            return self.get_dummy_value()
        else:
            return "Implement the function to send the actual value"

    def _subscribe_data(self):
        pass


class Sprinkler(Thing):
    def __init__(self, sprinkler_id, location, end_point, cert_filepath, private_key_file, ca_filepath):
        super().__init__(sprinkler_id, sprinkler_id, location, end_point, cert_filepath, private_key_file, ca_filepath)

    def _get_status(self):
        return self._status

    def _set_status(self, status):
        self._status = status

    def _publish_heartbeat(self):
        heartbeat_topic = utilities.get_topic(self.location, self.thing_parent, self.thing_id, "heartbeat")
        self._data['heartbeat'] = True
        self._send_message(heartbeat_topic)

    def _publish_data(self):
        pass

    def _read_message(self):
        pass

    def _subscribe_data(self):
        pass
