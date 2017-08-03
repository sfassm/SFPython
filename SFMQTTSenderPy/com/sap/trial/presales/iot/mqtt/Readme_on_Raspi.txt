 Sensor Scripts:
 
0) Download client_certificate.zip file from IoT Services for your device
and extract client certificate and plain private key from ZIP file into PEM files.
'create_certificate <name_of_the_downloaded_ZIP> <your_directory_with_the_downloaded_ZIP>'


1) Connect DHT11 sensor (blue one) for temp + humidity to 
Raspberry Pi: GRND = PIN6, Data=PIN7 (=Port4), VCC=PIN1

2) Test sensor with script:
a. Adjust sensor type in dot.read_retry(dht.DHT11/22, gpio_port)
b. sudo python AdafruitDHTTest.py

3) Adjust:
- DeviceID: <MAC address under which device was registered with IoT Services>
- LogNodeAddr: <Address_of_Sensor_connected_to_the_device>
- CERTIFICATE_FILE: extracted client_certificate.pem
- PLAIN_PRIVATE_KEY_FILE: extracted privat_key.pem (plain)
- sending intervall of data in SFRaspPiMQTTsSender4SAPIotSvc4.py

4) Check whether SFRaspPiMQTTsSender4SAPIotSvc4.py is already running (autostarted by
file /etc/init/autostart_pi_sensor_scripts.conf)
ps aux | grep autostart_pi_sensro_scripts.conf




