# ora_iotcs_sim
###### HTTP Connector Simulator for Oracle IoT Intelligent Apps Cloud Sevice

###### Create Simulator ini file : iotcs_sim.ini 
###### All sections are mandatory. [IOTCS_CONNECTION], [SENSOR_ATTRIBUTES], [LOCATION_ATTRIBUTES]

###### [IOTCS_CONNECTION]
###### IOTCS_HTTP_CONNECTOR_URL: IoT Cloud Service HTTP Connector URL.
###### IOTCS_USER=USER ID for IoT Cloud Service
###### IOTCS_PASSWORD= Password for IoT Cloud Service
###### MESSAGE_INTERVAL= Message interval defined in seconds (MESSAGE_INTERVAL=5 means 1 message every 5 seconds)

###### You can add additional sensor attributes attr1, attr2, attr3, attr4, attr5,..,attr(n)

###### [SENSOR_ATTRIBUTES]
###### sensor attribute description
###### name: sensor attribute name as defined in device model
###### min: minimum numeric simulated value for sensor
###### max: maximum numeric simulated value for sensor
###### function: pattern used to generate simulated data. available options: random, sin, cos

###### [LOCATION_ATTRIBUTES]
###### ora_latitude: latitude parameter for device location
###### ora_longitude: longitude parameter for device location


'''
#################################### Sample Simulator File ####################################
[IOTCS_CONNECTION]
IOTCS_HTTP_CONNECTOR_URL=https://<iotserviceurl>/cgw/<connector_name>
IOTCS_USER=<USERID>
IOTCS_PASSWORD=<PASSWORD>
MESSAGE_INTERVAL=1

[SENSOR_ATTRIBUTES]
attr1={"name":"temperature" , "min":40 , "max":50 , "function":"cos"}
attr2={"name":"humidity" , "min":80 , "max":100 , "function":"random"}
attr3={"name":"vibration" , "min":20 , "max":30 , "function":"sin"}
attr4={"name":"flow_rate" , "min":450 , "max":500 , "function":"random"}

[LOCATION_ATTRIBUTES]
ora_latitude=3.1174073
ora_longitude=101.6758658
'''
