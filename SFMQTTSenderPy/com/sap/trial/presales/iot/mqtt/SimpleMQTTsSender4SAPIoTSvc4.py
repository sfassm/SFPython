'''
Created on 31 Jul 2017

@author: d069454
'''
import paho.mqtt.client as paho
import time
import json
import random

# capture receipt when successfully published
def on_publish(client, userdata, msg_id):
    print("on_publish called, msg_id: " + str(msg_id) + " successfully published.\n")

# Addresses and IDs are case-sensitive!!!    
DEVICE_ID = "10:12:68:FA:01"                        # Device physical address / Unique Address, e.g. MAC address '5e:0a:27:0d:79:f9:38:9b' WITH ':' separators
LOG_NODE_ADDR = "SF_Local_PAHO_UIClient_Sensor_1"   # Sensor address / physical address: "<simple_string_as_given>", e.g. "00:00:00:02"
PUB_TOPIC = "measures/" + DEVICE_ID                 # MQTT pub topic

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
        #data = json.dumps({"profileId":4,"measureIds":[510],"values": ['{}'.format(temperature), '{}'.format(humidity)],"logNodeAddr":logNodeAddrStr})
        data = json.dumps({"profileId":4,"measureIds":[510],"values": ['{}'.format(temperature), '{}'.format(humidity)],"logNodeAddr":LOG_NODE_ADDR})
        print("Publishing message under topic=" + PUB_TOPIC + ", JSON body: " + data)
        # Publish data:
        (rc, msg_id) = mqttclnt.publish(PUB_TOPIC, data)
        # wait some time to read again sensor values
        time.sleep(timeIntervall)
    
    except IOError:
        print ("Error")
 
