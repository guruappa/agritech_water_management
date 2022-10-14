import configparser
from pyowm.owm import OWM
import confuse

file_path = "water_management.ini"
things_config_file = "things.yaml"
config = configparser.ConfigParser()
config.read(file_path)
things_config = confuse.Configuration('water_management', __name__)
things_config.set_file(things_config_file)


def get_owm_key():
    own_key = config['OWM']['API_KEY']
    return own_key


def get_location_data(district, country):
    api_key = get_owm_key()
    owm = OWM(api_key)
    reg = owm.city_id_registry()
    loc = reg.locations_for(district, country=country)[0]
    return loc


def get_publish_frequency():
    return config['Publish']['frequency']


def get_topic(location, sprinkler, sensor, topic_type):
    if topic_type in ['publish', 'subscribe', 'heartbeat']:
        topic_type += "_topic"
        if sprinkler and sensor:
            return things_config['locations'][location]['sprinklers'][sprinkler]['sensors'][sensor][topic_type].get()
        elif sprinkler and not sensor:
            return things_config['locations'][location]['sprinklers'][sprinkler][topic_type].get()
        else:
            return "Not Configured"
    else:
        return f"Unknown Topic Type : {type}"


def get_sprinklers_list():
    return [sprinkler for sprinkler in things_config['sprinklers'].get().keys()]


def get_sensors_list(sprinkler):
    return [sensor for sensor in things_config['sprinklers'][sprinkler]['sensors'].get().keys()]


def get_mqtt_endpoint():
    return config['AWS_MQTT']['endpoint']


def get_mqtt_aws_root_certificate():
    return config['AWS_MQTT']['aws_root_cert']


def get_mqtt_certificate():
    return config['AWS_MQTT']['certificate']


def get_mqtt_private_key():
    return config['AWS_MQTT']['private_key']
