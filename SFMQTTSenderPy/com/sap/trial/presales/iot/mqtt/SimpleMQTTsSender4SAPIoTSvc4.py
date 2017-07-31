'''
Created on 31 Jul 2017

@author: d069454
'''
import paho.mqtt.client as paho
import time
import json

# capture receipt when successfully published
def on_publish(client, userdata, msg_id):
    print("on_publish called, msg_id: " + str(msg_id) + " successfully published.\n")
    
DEVICE_ID = "10:12:68:FA:01"                        # Device physical address / Unique Address, e.g. MAC address '5e0a270d79f9389b' w/o ':' separators
LOG_NODE_ADDR = "SF_Local_PAHO_UIClient_Sensor_1"   # Sensor address / physical address: "60c8faf8d6560b7c"
PUB_TOPIC = "measures/" + DEVICE_ID                 # MQTT pub topic

i = 1
timeIntervall = 15
temperature = 20
humidity = 40

mqttclnt = paho.Client()
mqttclnt.on_publish = on_publish
#mqttclnt.username_pw_set("root#0", "KYTAcbyNY5qlsmh")
mqttclnt.tls_set(certfile="certificate.pem", keyfile="plainkey.pem") # downloaded from IoTServices for this device as *.ks file, needs to be converted into *.pem files
mqttclnt.connect("iotae-beta03.eu10.cp.iot.sap", 8883)
#data = json.dumps({"profileId":4,"measureIds":[510],"values": ['{}'.format(temperature), '{}'.format(humidity)],"logNodeAddr":logNodeAddrStr})
data = json.dumps({"measureIds":[510],"values": ['{}'.format(temperature), '{}'.format(humidity)],"logNodeAddr":LOG_NODE_ADDR})
print("Publishing message under topic=" + PUB_TOPIC + ", JSON body: " + data)
 
for i in range(1, 3):
    (rc, msg_id) = mqttclnt.publish(PUB_TOPIC, data)
    time.sleep(timeIntervall)
