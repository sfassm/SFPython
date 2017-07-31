# Simple MQTT over SSL subscriber
# Idea from https://stackoverflow.com/questions/24637763/wrapping-mqtt-data-in-ssl-certificate-while-sending-it-to-mqtt-broker#24652059

'''
Created on 28 Jul 2017

@author: d069454
'''
#!/usr/bin/env python
import paho.mqtt.client as paho

def on_subscribe(client, userdata, msg_id, granted_qos):
    print("Subscribed: "+str(msg_id)+" "+str(granted_qos))
    
def on_message(clnt, userdata, msg_id):
    print(msg_id.topic+" "+str(msg_id.payload))

mqttclnt = paho.Client()
mqttclnt.on_subscribe = on_subscribe
mqttclnt.on_message = on_message

# SF: For test.mosquitto.org test server
mqttclnt.tls_set(certfile="certificate.pem", keyfile="plainkey.pem") # http://test.mosquitto.org/ssl/mosquitto.org.crt
print ("Next, call Connect:")
mqttclnt.connect("iotae-beta03.eu10.cp.iot.sap", 8883)
print ("Next, call subscribe:")
msg_id = mqttclnt.subscribe("measures\/10:12:68:FA:01", qos=1)
print ("Entering loop")
mqttclnt.loop_forever()