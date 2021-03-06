import requests
from requests.auth import HTTPBasicAuth
import logging
import configparser
import random
import numpy as np
import json
import time


# Check Config
def checkConfig():
    try:
        assert 'IOTCS_CONNECTION' in config, "Error: IoTCS Connection Details missing in config"
        assert 'SENSOR_ATTRIBUTES' in config, "Error: Sensor Attributes Details missing in config"
        assert 'DEVICE_ATTRIBUTES' in config, "Error: Device Attributes Details missing in config"
    except AssertionError as err:
        logging.error("Sections missing in config [IOTCS_CONNECTION],[SENSOR_ATTRIBUTES],[DEVICE_ATTRIBUTES]")
        print(err.args[0])
        exit(0)

def sendDataToIoT(IoTURL,iotUser,iotPassword,data,packetcount):
    try:
        response = requests.post(IoTURL, auth=HTTPBasicAuth(iotUser, iotPassword), json=data)
        logging.debug(str(response)+' -> Sending data to IoTCS : '+str(data))
        print("[{}]sending data to {}:{}".format(packetcount,IoTURL, str(data)))
    except Exception as err:
        logging.error(err)
        print("Create HTTP Adaptor in IoTCS and try again!!")
        exit(0)

def sinWaveGenerator(tm,amplitude=5,wavelength=100,phase=0,axis=40):
    frequency = 1 / wavelength
    sinewave = amplitude * np.sin(2 * np.pi * frequency * tm + phase) + axis
    return round(sinewave,4)

def cosWaveGenerator(tm, amplitude=5,wavelength=100,phase=0,axis=40):
    frequency = 1 / wavelength
    coswave = amplitude * np.cos(2 * np.pi * frequency * tm + phase) + axis
    return round(coswave,4)

def getSensorValue(tm1, minRange=1, maxRange=2, functiontype='random'):
    if functiontype=='random':
        return round(random.randint(minRange,maxRange) + random.random(),2)
    elif functiontype=='sin':
        return sinWaveGenerator(tm1,(maxRange-minRange)/2,wavelength=100,axis=(maxRange+minRange)/2)
    elif functiontype=='cos':
        return cosWaveGenerator(tm1,(maxRange-minRange)/2,wavelength=100,axis=(maxRange+minRange)/2)

def getConnectionDetails():
    try:
        assert "IOTCS_HTTP_CONNECTOR_URL" in config["IOTCS_CONNECTION"],"IoTCS HTTP Connector URL is missing IOTCS_HTTP_CONNECTOR_URL=<URL>"
        assert "IOTCS_USER" in config["IOTCS_CONNECTION"], "IoTCS User is missing IOTCS_USER=<username>"
        assert "IOTCS_PASSWORD" in config["IOTCS_CONNECTION"], "IoTCS Password is missing IOTCS_PASSWORD=<password>"
        assert "MESSAGE_INTERVAL" in config["IOTCS_CONNECTION"], "IoTCS Message Interval is missing MESSAGE_INTERVAL=<5s>"
    except AssertionError as err:
        logging.error("Some of connection details are missing")
        print(err.args[0])
        exit(0)
    else:
        return config["IOTCS_CONNECTION"]["IOTCS_HTTP_CONNECTOR_URL"].replace('"',''),config["IOTCS_CONNECTION"]["IOTCS_USER"].replace('"',''),config["IOTCS_CONNECTION"]["IOTCS_PASSWORD"].replace('"',''),config["IOTCS_CONNECTION"]["MESSAGE_INTERVAL"]

def getSensorAttributes():
    sensorData = dict()
    for sensor_attribute in config["SENSOR_ATTRIBUTES"]:
        sensorData[sensor_attribute]=config["SENSOR_ATTRIBUTES"][sensor_attribute]
    return sensorData

def getLocationAttributes():
    try:
        assert "latitude" in config[
            "DEVICE_ATTRIBUTES"], "Latitude value is missing latitude=3.1174073"
        assert "longitude" in config["DEVICE_ATTRIBUTES"], "Longitude value is missing longitude=101.6758658"
    except AssertionError as err:
        logging.error("Location Parameters are missing")
        print(err.args[0])
        exit(0)
    else:
        return config["DEVICE_ATTRIBUTES"]["latitude"],config["DEVICE_ATTRIBUTES"]["longitude"]

def getDeviceID():
    try:
        assert "deviceid" in config[
            "DEVICE_ATTRIBUTES"], "deviceid value is missing [deviceid=SENSOR12345]"
    except AssertionError as err:
        logging.error("deviceid is missing")
        print(err.args[0])
        exit(0)
    else:
        return config["DEVICE_ATTRIBUTES"]["deviceid"]


## Main Program
tm = np.arange(0, 100, 1 / 6);
wavePointCounter = 0
logging.basicConfig(format='%(asctime)s %(message)s' , datefmt='%Y%m%d-%H:%M:%S %p  <-->', level=logging.INFO)
config = configparser.ConfigParser()
config.read('iotcs_sim.cfg')
checkConfig()
http_connector_url, iot_user, iot_password, message_interval = getConnectionDetails()
latitude, longitude = getLocationAttributes()
deviceid = getDeviceID()
sensor_attributes = getSensorAttributes()
unpackedSensors = list()
for sensor in sensor_attributes:
    unpackedSensors.append(json.loads(sensor_attributes[sensor]))

while(1):
    iot_data = dict()
    for sensor in unpackedSensors:
        iot_data[sensor["name"]]=getSensorValue(tm[wavePointCounter],sensor["min"],sensor["max"],sensor["function"])
    iot_data["latitude"] = latitude
    iot_data["longitude"] = longitude
    iot_data["deviceid"] = deviceid
    sendDataToIoT(http_connector_url, iot_user, iot_password, iot_data,wavePointCounter)

    wavePointCounter+=1
    if wavePointCounter == 100:
        wavePointCounter=0
    time.sleep(int(message_interval))
