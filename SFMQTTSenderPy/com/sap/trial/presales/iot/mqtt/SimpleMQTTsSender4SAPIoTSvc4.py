'''
Created on 31 Jul 2017

Simple example of using the PAHO Python lib for publishing messages to SAP IoT Services 4.x
(Values are created randomly for demonstrating purposes.)
Important: 
The client certificate and private key which are retrieved in a client.ks file from 
SAP IoT Services for the given device must be extracted and provided as *.pem files

@author: d069454
'''
import paho.mqtt.client as paho
import time
import json
import random

# Capture receipt when successfully published
def on_publish(client, userdata, msg_id):
    print("on_publish called, msg_id: " + str(msg_id) + " successfully published.\n")

# Addresses and IDs are case-sensitive!!!    
#DEVICE_ID = "10:12:68:FA:01"                        # Device physical address / Unique Address, e.g. MAC address '5e:0a:27:0d:79:f9:38:9b' WITH ':' separators
#LOG_NODE_ADDR = "SF_Local_PAHO_UIClient_Sensor_1"   # Sensor address / physical address: "<simple_string_as_given>", e.g. "00:00:00:02"
#DEVICE_ID = "B8:27:EB:C3:1a:AA"                        # Device physical address / Unique Address, e.g. MAC address '5e:0a:27:0d:79:f9:38:9b' WITH ':' separators
#LOG_NODE_ADDR = "D069454_Sensor_DHT11_Rasp301"   # Sensor address / physical address: "<simple_string_as_given>", e.g. "00:00:00:02"
DEVICE_ID = "00:87:40:71:C2:AE"
LOG_NODE_ADDR = "D069454_Sensor_DHT11_RaspBplus"
PUB_TOPIC = "measures/" + DEVICE_ID                 # MQTT pub topic
CERTIFICATE_FILE = "clientcerts/sfraspb301_client_certificate.pem"      # location of device's certificate file (extracted from downloaded client.ks)
PLAIN_PRIVATEKEY_FILE = "clientcerts/sfraspb301_client_certificate_privatekey_plain.pem"    # location of file with device's plain private key (extracted from downloaded client.ks)

timeIntervall = 5

mqttclnt = paho.Client(client_id=DEVICE_ID)
mqttclnt.on_publish = on_publish
mqttclnt.tls_set(certfile=CERTIFICATE_FILE, keyfile=PLAIN_PRIVATEKEY_FILE) # downloaded from IoTServices for this device as *.ks file, needs to be converted into *.pem files
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
        # Wait some time (e.g. simulating reading potential sensor values)
        time.sleep(timeIntervall)
    
    except IOError:
        print ("Error")
 
