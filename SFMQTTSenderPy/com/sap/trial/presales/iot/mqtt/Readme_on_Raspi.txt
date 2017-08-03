 Sensor Scripts:

1) Connect DHT11 sensor (blue one) for temp + humidity to 
Raspberry Pi: GRND = PIN6, Data=PIN7 (=Port4), VCC=PIN1

2) Test sensor with script:
a. Adjust sensor type in dot.read_retry(dht.DHT11/22, gpio_port)
b. sudo python AdafruitDHTTest.py

3) Adjust sending intervall of data in SFRaspPiMQTTsSender4SAPIotSvc4.py

4) Check whether SFRaspPiMQTTsSender4SAPIotSvc4.py is already running (autostarted by
file /etc/init/autostart_pi_sensor_scripts.conf)
ps aux | grep autostart_pi_sensro_scripts.conf




