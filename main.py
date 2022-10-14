from water_management import utilities
from water_management.Thing import Sensor
import time as t


def setup_sprinkler(sprinkler):
    pass


def setup_sprinklers():
    sprinklers = utilities.get_sprinklers_list()

    for sprinkler in sprinklers:
        sensors = utilities.get_sensors_list(sprinkler)


def test_sensor():
    sensor_id = "sensor_11"
    sprinkler = "sprinkler_1"
    location = "location_1"
    end_point = "a3qe69pk26zn9j-ats.iot.us-east-1.amazonaws.com"
    cert_filepath = "certificates/location_1_sensor_11.cert.pem"
    private_key_file = "certificates/location_1_sensor_11.private.key"
    ca_filepath = "certificates/root-CA.crt"
    sensor_11 = Sensor(sensor_id, sprinkler, location, end_point, cert_filepath, private_key_file, ca_filepath)

    print("Publish Start")

    for i in range(10):
        sensor_11._publish_data()
        t.sleep(0.1)

    print("Publish Stopped")


if __name__ == '__main__':
    test_sensor()

