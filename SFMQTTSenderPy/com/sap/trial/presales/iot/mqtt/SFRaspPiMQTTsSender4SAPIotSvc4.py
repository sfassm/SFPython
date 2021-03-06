
'''
Simple example of using the PAHO Python lib for publishing messages to SAP IoT Services 4.x
Values are read from DHT11 Temp&Humidity sensor connected to Raspberry CPIO port 4 (Pin7)
using the Adafruit Python library.

Important: 
The client certificate and private key which are retrieved in a client.ks file from 
SAP IoT Services for the given device must be extracted and provided as *.pem files

Created on 28 Jul 2017

@author: d069454
'''
import paho.mqtt.client as paho
import time
import json
import Adafruit_DHT as dht # only available on Raspberry Pi

# Capture receipt when successfully published
def on_publish(client, userdata, msg_id):
    print("on_publish called, msg_id: " + str(msg_id) + " successfully published.\n")

# Addresses and IDs are case-sensitive!!!    
DEVICE_ID = "00:87:40:71:C2:AE"                     # Device physical address / Unique Address, e.g. MAC address '5e:0a:27:0d:79:f9:38:9b' WITH ':' separators
LOG_NODE_ADDR = "D069454_Sensor_DHT11_RaspBplus"    # Sensor address / physical address: "<simple_string_as_given>", e.g. "00:00:00:02"
PUB_TOPIC = "measures/" + DEVICE_ID                 # MQTT pub topic
GPIO_SENSOR_PORT = 4                                # port to which DHT sensor is connected on Raspberry Pi GPIO, e.g. Port4=PIN7
CERTIFICATE_FILE = "client_certificate.pem"         # location of device's certificate file (extracted from downloaded client.ks)
PLAIN_PRIVATEKEY_FILE = "client_certificate_privatekey_plain.pem"    # location of file with device's plain private key (extracted from downloaded client.ks)

timeIntervall = 5

mqttclnt = paho.Client(client_id=DEVICE_ID)
mqttclnt.on_publish = on_publish
#mqttclnt.username_pw_set("<user>#<tenant>", "<pwd>")
mqttclnt.tls_set(certfile=CERTIFICATE_FILE, keyfile=PLAIN_PRIVATEKEY_FILE) # downloaded from IoTServices for this device as *.ks file, needs to be converted into *.pem files
mqttclnt.connect("iotae-beta03.eu10.cp.iot.sap", 8883)

while True:
    try:
        # Read values from DHT sensor connected to Raspberry Pi GPIO using Adafruit library
        humidity, temperature = dht.read_retry(dht.DHT11, GPIO_SENSOR_PORT)
        # Fixed values for testing only
        humidity, temperature = [20, 40]
        humidity = int(humidity)
        temperature = int(temperature)

        data = json.dumps({"profileId":4,"measureIds":[510],"values": ['{}'.format(temperature), '{}'.format(humidity)],"logNodeAddr":LOG_NODE_ADDR})
        print("Publishing message under topic=" + PUB_TOPIC + ", JSON body: " + data)
        # Publish data:
        (rc, msg_id) = mqttclnt.publish(PUB_TOPIC, data)
        # Wait some time (e.g. simulating reading potential sensor values)
        time.sleep(timeIntervall)
    
    except IOError:
        print ("Error")



    