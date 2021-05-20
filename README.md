## HTTP Connector Simulator for Oracle IoT Intelligent Apps Cloud Sevice
This HTTP Connector Simulator for Oracle IoT Intelligent Apps can run on microcontroller development boards like **Raspberry Pi** that can run python 3.6 and above or any computer system (WIN/MacOS/Linux).

### Steps to Follow

#### 1. Install Python 
Install Python 3.6 or above
###### (For Linux/Unix)
https://docs.python-guide.org/starting/install3/linux/
###### (For Windows)
https://docs.python-guide.org/starting/install3/win/
###### (For Mac)
https://docs.python-guide.org/starting/install3/osx/
#### 2. Copy project source
`git clone https://github.com/pranavmahajan074/ora_iotcs_sim.git`

#### 3. Create and Activate Virtual Environment
```
cd ora_iotcs_sim/
ls -ltr
python3.6 -m venv venv
source venv/bin/activate
```
#### 4. Upgrade pip and Install Dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```
#### 5. Create Simulator Config

###### Create Simulator config file : iotcs_sim.cfg 
All sections are mandatory. [IOTCS_CONNECTION], [SENSOR_ATTRIBUTES], [LOCATION_ATTRIBUTES]

|Section|Description|
|---|---|
|**[IOTCS_CONNECTION]**|This section provides device connectivity parameters|
|`IOTCS_HTTP_CONNECTOR_URL`| IoT Cloud Service HTTP Connector URL|
|`IOTCS_USER`|USER ID for IoT Cloud Service|
|`IOTCS_PASSWORD`| Password for IoT Cloud Service|
|`MESSAGE_INTERVAL`| Message interval defined in seconds (MESSAGE_INTERVAL=5 means 1 message every 5 seconds)|
|`SIMULATION`| Define whether data is simulated or from sensor (YES - for Simulated/NO - Live Sensor)|

|Section|Description|
|---|---|
|**[SENSOR_ATTRIBUTES]**| This section includes all sensor attributes that need to be simulated.|
`attr1`|You can add additional sensor attributes `attr1`, `attr2`, `attr3`, `attr4`, `attr5`,..,`attr(n)`|
|`name`| sensor attribute name as defined in device model|
|`min`| minimum numeric simulated value for sensor|
|`max`| maximum numeric simulated value for sensor|
|`function`| pattern used to generate simulated data. available options: `random`, `sin`, `cos`|

|Section|Description|
|---|---|
|**[DEVICE_ATTRIBUTES]**| Provide device ID and location attributes for device|
|`deviceid`| Unique device ID or Serial no.|
|`latitude`| latitude parameter for device location|
|`longitude`| longitude parameter for device location|

|Section|Description|
|---|---|
|**[RASPBERRY_PI_IO]**| Provide details for GPIO Connection for Sensors|
|`GPIO_TEMPERATURE`| GPIO PIN No.|
|`GPIO_HUMIDITY`| GPIO PIN No.|
|`GPIO_VIBRATION`| GPIO PIN No.|
#### Sample Configuration File : iotcs_sim.cfg

```
#################################### Sample Simulator File ####################################
[IOTCS_CONNECTION]
IOTCS_HTTP_CONNECTOR_URL=https://<iotserviceurl>/cgw/<connector_name>
IOTCS_USER=<USERID>
IOTCS_PASSWORD=<PASSWORD>
MESSAGE_INTERVAL=1
SIMULATION=YES

[SENSOR_ATTRIBUTES]
attr1={"name":"temperature" , "min":25 , "max":30 , "function":"sin"}
attr2={"name":"humidity" , "min":90 , "max":100 , "function":"random"}
attr3={"name":"vibration" , "min":1 , "max":2 , "function":"sin"}

[DEVICE_ATTRIBUTES]
deviceid=SENSOR12345
latitude=3.1174073
longitude=101.6758658


[RASPBERRY_PI_IO]
GPIO_TEMPERATURE=GPIO2
GPIO_HUMIDITY=GPIO3
GPIO_VIBRATION=GPIO4
```

#### 6. Run Program
`python main.py`
