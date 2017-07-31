# SF: Python script based on the officially available MQTT Python client
# see https://eclipse.org/paho/clients/python/
# more details are maintained in the README.TXT file of this project
# It uses the SAP Cloud Platform as message broker.
# SSL parts of the code are from https://stackoverflow.com/questions/24637763/wrapping-mqtt-data-in-ssl-certificate-while-sending-it-to-mqtt-broker#24652059

'''
Created on 28 Jul 2017

@author: d069454
'''
import paho.mqtt.client as paho
import time

# capture receipt when successfully published
def on_publish(client, userdata, msg_id):
    print("on_publish called, msg_id: " + str(msg_id) + " successfully published.\n")
    
logNodeAddrStr = "SF_Local_PAHO_UIClient_Sensor_1"
i = 1
# temp_str = '{0:0.1f}'.format(20)
# humid_str = '{0:0.1f}'.format(40)
temp_str = "20"
humid_str = "40"

mqttclnt = paho.Client()
mqttclnt.on_publish = on_publish
mqttclnt.tls_set(certfile="certificate.pem", keyfile="plainkey.pem") # downloaded from IoTServices for this device as *.ks file, needs to be converted into *.pem files
mqttclnt.connect("iotae-beta03.eu10.cp.iot.sap", 8883)
print("Message Body: " + "{\"profileId\":4,\"measureIds\":[510],\"values\":[\"" + temp_str + "\",\"" + humid_str + "\"],\"logNodeAddr\":\"" + logNodeAddrStr + "\"}")

for i in range(1, 10):
#     temperature = 20 +i
#     humidity = 40 -i
#     temp_str = '{0:0.1f}'.format(temperature)
#     humid_str = '{0:0.1f}'.format(humidity)
    
    if i <= 5 :
        print "Temperature smaller or equal than 25, sent to iotae-beta03.eu10.cp.iot.sap with temperature = " + temp_str + "C" + ", humidity = " + humid_str + "%"
        # w/o return-receipt: mqttclnt.publish("measures/10:12:68:FA:01", '{0:0.1f}'.format(temperature))
        (rc, msg_id) = mqttclnt.publish("measures/10:12:68:FA:01", "{\"profileId\":4,\"measureIds\":[510],\"values\":[\"" + temp_str + "\",\"" + humid_str + "\"],\"logNodeAddr\":\"" + logNodeAddrStr + "\"}")
    else:
        print "Temperature larger than 25, sent to iotae-beta03.eu10.cp.iot.sap with humidity = " + temp_str + "C, humidity = " + humid_str + "%\n"
        mqttclnt.publish("measures/10:12:68:FA:01", "{\"profileId\":4,\"measureIds\":[510],\"values\":[\"" + temp_str + "\",\"" + humid_str + "\"],\"logNodeAddr\":\"" + logNodeAddrStr + "\"}")
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