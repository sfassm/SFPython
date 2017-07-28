# SF: Python script based on the officially available MQTT Python client
# see https://eclipse.org/paho/clients/python/
# more details are maintained in the README.TXT file of this project
# 
'''
Created on 28 Jul 2017

@author: d069454
'''
#!/usr/bin/env python
import paho.mqtt.publish as publish
import time
temp_sensor = 0
i = 1
for i in range(1, 10):
    temperature = 20 +i
    humidity = 40 -i
    if i <= 5 :
        print "Temperature smaller or equal than 25, sent to test.mosquitto.org with msg body = " + '{0:0.1f}'.format(temperature) + "\n"
        publish.single("office/temperature", '{0:0.1f}'.format(temperature), hostname="test.mosquitto.org")
    else:
        print "Temperature larger than 25, sent to test.mosquitto.org with msg body = " + '{0:0.1f}'.format(temperature) + "\n"
        publish.single("office/temperature", '{0:0.1f}'.format(temperature), hostname="test.mosquitto.org")
    time.sleep(5)
        
# def readTemperature():
#     while True:
#         try:
#             temperature = grovepi.temp(temp_sensor, '1,2')
#             publish.single("office/temperature", '{0:0.1f}'.format(temperature), hostname="192.168.10.200")
#             time.sleep(5)
#         except KeyboardInterrupt:
#             break
#         except IOError:
#             print "IOError happened"
# readTemperature()