'''
Created on 28 Jul 2017

@author: d069454
'''
#!/usr/bin/env python
import paho.mqtt.client as paho
import time

# capture receipt when successfully published
def on_publish(client, userdata, msg_id):
    print("on_publish called, msg_id: " + str(msg_id) + " successfully published.\n")
    
temp_sensor = 0
i = 1
mqttclnt = paho.Client()
mqttclnt.on_publish = on_publish
mqttclnt.tls_set("Certificate_from_mosquitto.org.crt") # http://test.mosquitto.org/ssl/mosquitto.org.crt
mqttclnt.connect("test.mosquitto.org", 8883)

for i in range(1, 10):
    temperature = 20 +i
    humidity = 40 -i
    if i <= 5 :
        print "Temperature smaller or equal than 25, sent to test.mosquitto.org with msg body = " + '{0:0.1f}'.format(temperature)
        # w/o return-receipt: mqttclnt.publish("measures/10:12:68:FA:01", '{0:0.1f}'.format(temperature))
        (rc, msg_id) = mqttclnt.publish("measures/10:12:68:FA:01", '{0:0.1f}'.format(temperature))
    else:
        print "Temperature larger than 25, sent to test.mosquitto.org with msg body = " + '{0:0.1f}'.format(temperature) + "\n"
        mqttclnt.publish("measures/10:12:68:FA:01", '{0:0.1f}'.format(temperature))
    time.sleep(5)
