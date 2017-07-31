# Simple MQTT over SSL subscriber
# Idea from https://stackoverflow.com/questions/24637763/wrapping-mqtt-data-in-ssl-certificate-while-sending-it-to-mqtt-broker#24652059

'''
Created on 28 Jul 2017

@author: d069454
'''
#!/usr/bin/env python
import paho.mqtt.client as paho
# Addresses and IDs are case-sensitive!!!    
DEVICE_ID = "10:12:68:FA:01"                        # Device physical address / Unique Address, e.g. MAC address '5e:0a:27:0d:79:f9:38:9b' WITH ':' separators
LOG_NODE_ADDR = "SF_Local_PAHO_UIClient_Sensor_1"   # Sensor address / physical address: "<simple_string_as_given>", e.g. "00:00:00:02"
SUB_TOPIC = "measures/" + DEVICE_ID                 # MQTT pub topic
CERTIFICATE_FILE = "PahoUIClientCerts/certificate.pem"      # location of device's certificate file (extracted from downloaded client.ks)
PLAIN_PRIVATEKEY_FILE = "PahoUIClientCerts/plainkey.pem"    # location of file with device's plain private key (extracted from downloaded client.ks)

def on_subscribe(client, userdata, msg_id, granted_qos):
    print("Subscribed to topic="+str(msg_id.topic())+" with QoS="+str(granted_qos))
    
def on_message(client, userdata, msg_id):
    print("Received under topic=" + msg_id.topic+", msg_id= " + msg_id + " with payload=" + str(msg_id.payload))

mqttclnt = paho.Client(client_id=DEVICE_ID)
mqttclnt.on_subscribe = on_subscribe
mqttclnt.on_message = on_message

# SF: For test.mosquitto.org test server
mqttclnt.tls_set(certfile=CERTIFICATE_FILE, keyfile=PLAIN_PRIVATEKEY_FILE) # downloaded from IoTServices for this device as *.ks file, needs to be converted into *.pem files
mqttclnt.connect("iotae-beta03.eu10.cp.iot.sap", 8883)
(rc,msg_id) = mqttclnt.subscribe(SUB_TOPIC, 0)
if (rc == paho.MQTT_ERR_SUCCESS):
    print ("Subscription successfully craeted, rc=" + "{}".format(rc))
mqttclnt.loop_forever()