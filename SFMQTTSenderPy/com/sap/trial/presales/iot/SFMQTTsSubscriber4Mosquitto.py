# Simple MQTT over SSL subscriber
# Idea from https://stackoverflow.com/questions/24637763/wrapping-mqtt-data-in-ssl-certificate-while-sending-it-to-mqtt-broker#24652059

'''
Created on 28 Jul 2017

@author: d069454
'''
import paho.mqtt.client as paho

def on_message(clnt, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_message = on_message

# SF: For test.mosquitto.org test server
mqttc.tls_set("Certificate_from_mosquitto.org.crt") # http://test.mosquitto.org/ssl/mosquitto.org.crt
mqttc.connect("test.mosquitto.org", 8883)
mqttc.subscribe("measures/10:12:68:FA:01")
mqttc.loop_forever()