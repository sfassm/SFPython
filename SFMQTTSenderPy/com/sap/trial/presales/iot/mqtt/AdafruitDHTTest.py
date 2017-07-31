'''
Adafruit DHT Test program
-> simply checks whether the connected sensor is working 
using the Adafruit python lib

Created on 31 Jul 2017

@author: d069454
'''
# Install the Adafruit Python lib for your sensor, e.g. DHT (Humidity and Temperature sensor):
import Adafruit_DHT as dht

# Retrieve values (by providing the type of sensor and the GPIO port, e.g. PIN7=GPIO4
sensor = "DHT11"
gpio_port = 4
humidity, temperature = dht.read_retry(dht.DHT11, gpio_port)
humidity = int(humidity)
temperature = int(temperature)
print("Temp=" + '{}'.format(temperature) + ", humidity=" + '{}'.format(humidity))