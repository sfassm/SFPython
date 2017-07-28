  MQTTs Publisher Client
 ========================
 
 This is based on officially available source code from PAHO.
 Follow these steps to install the latest Paho client so that the module is available of our scripts:
 
 1. Download Paho client:
    check out: https://eclipse.org/paho/clients/python/
 	git clone https://github.com/eclipse/paho.mqtt.python.git 
2. Install the Paho client:
	cd paho.mqtt.python
	sudo python setup.py install
Alternatively use installation of MQTT python client: 
	pip install paho-mqtt
	
 3. Write a test client and connect to MQTT test broker: test.mosquitto.org
 
 4. Use MQTTs
 - see https://stackoverflow.com/questions/24637763/wrapping-mqtt-data-in-ssl-certificate-while-sending-it-to-mqtt-broker#24652059