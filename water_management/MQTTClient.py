import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
from water_management import utilities

ENDPOINT = utilities.get_mqtt_endpoint()
CLIENT_ID = utilities.get_mqtt_client()
MQTT_CERTIFICATE = utilities.get_mqtt_certificate()
MQTT_PRIVATE_KEY = utilities.get_mqtt_private_key()
MQTT_AWS_ROOT_CA = utilities.get_mqtt_aws_root_certificate()

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(MQTT_AWS_ROOT_CA, MQTT_PRIVATE_KEY, MQTT_CERTIFICATE)


def get_mqtt_client():
    return myAWSIoTMQTTClient
