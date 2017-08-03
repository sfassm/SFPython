  MQTTs Publisher Client
 ========================
 
 This is based on officially available source code from PAHO.
 Follow these steps to install the latest Paho client so that the module is available of our scripts:
 
 1. Download Paho client:
    check out: https://eclipse.org/paho/clients/python/
 	git clone https://github.com/eclipse/paho.mqtt.python.git 
2. Install the Paho client:
	cd paho.mqtt.python
	sudo python setup.py install
Alternatively use installation of MQTT python client: 
	pip install paho-mqtt
	
 3. Write a test client and connect to MQTT test broker: test.mosquitto.org
 
 4. Use MQTTs
 - see https://stackoverflow.com/questions/24637763/wrapping-mqtt-data-in-ssl-certificate-while-sending-it-to-mqtt-broker#24652059
 
 5. Connect DHT Sensor (Temp+Humidity) to Pi (VCC=PIN1, GRND=PIN6, DATA=PIN7=GPIO-Port4)
 
 6. Use Adafruit lib for reading sensor data
 
  EXAMPLES
 ==========
1) Example Python Script using adafruit lib:
import Adafruit_DHT as dht
humidity, temperature = dht.read_retry(dht.DHT22, 4)
humidity = int(humidity)
temperature = int(temperature)
print("Temp=" + temperature + ", humidity=" + humidity)
 
2) MQTT Publisher to SAP IoT 4.x services:
# Addresses and IDs are case-sensitive!!!    
DEVICE_ID = "10:12:68:FA:01"                        # Device physical address / Unique Address, e.g. MAC address '5e:0a:27:0d:79:f9:38:9b' WITH ':' separators
LOG_NODE_ADDR = "SF_Local_PAHO_UIClient_Sensor_1"   # Sensor address / physical address: "<simple_string_as_given>", e.g. "00:00:00:02"
PUB_TOPIC = "measures/" + DEVICE_ID                 # MQTT pub topic

timeIntervall = 5

mqttclnt = paho.Client(client_id=DEVICE_ID)
mqttclnt.on_publish = on_publish
#mqttclnt.username_pw_set("root#0", "KYTAcbyNY5qlsmh")
mqttclnt.tls_set(certfile="certificate.pem", keyfile="plainkey.pem") # downloaded from IoTServices for this device as *.ks file, needs to be converted into *.pem files
mqttclnt.connect("iotae-beta03.eu10.cp.iot.sap", 8883)

while True:
    try:
        # Create some random values
        humidity = random.randint(0, 100)
        temperature = random.randint(10, 30)
        data = json.dumps({"profileId":4,"measureIds":[510],"values": ['{}'.format(temperature), '{}'.format(humidity)],"logNodeAddr":LOG_NODE_ADDR})
        print("Publishing message under topic=" + PUB_TOPIC + ", JSON body: " + data)
        # Publish data:
        (rc, msg_id) = mqttclnt.publish(PUB_TOPIC, data)
        # wait some time to read again sensor values
        time.sleep(timeIntervall)
    
    except IOError:
        print ("Error")