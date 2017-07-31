'''
Created on 31 Jul 2017

@author: d069454
'''

#!/usr/env/python

import requests
import json
import time
import random

# MAC address without '-' or ':' b827eb9d3f4c
# URL: https://ekt3.hcp.iot.sap/iot/gateway/rest/measures/<MAC_address>
DEVICE_ID = "5e0a270d79f9389b"      # Device physical address / Unique Address, e.g. MAC address '5e0a270d79f9389b' w/o ':' separators
LOG_NODE_ADDR = "60c8faf8d6560b7c"  # Sensor address / physical address: "60c8faf8d6560b7c"
timeIntervall = 5

while True:
    try:
        # Create some random values
        humidity = random.randint(0, 100)
        temperature = random.randint(10, 30)
        # Build HTTPs request:
        headers = {'content-type': 'application/json'} 
        data = json.dumps({"measureIds":[510], "values": ['{}'.format(temperature), '{}'.format(humidity)],"profileId":4,"logNodeAddr":LOG_NODE_ADDR})
        # Issue HTTPs request
        httpsrequ = requests.post('https://iotae-beta03.eu10.cp.iot.sap/iot/gateway/rest/measures/{}'.format(DEVICE_ID),
                          data=data,
                          headers=headers,
                          cert=('client_certificate.pem','client_certificate_privatekey_plain.pem'),
                          timeout=5)
        
        # Deal with returned HTTP status code:
        if httpsrequ.status_code == 200:
            print('Sent data weather data temperature: {}, humidity: {}'.format(temperature, humidity))
        else:
            print('===== Error sending data =====')
            print('==> HTTP Response: %d', httpsrequ.status_code)
            print('==> HTTP Content: %d', httpsrequ.content)
            responseCode = httpsrequ.status_code
            print ("==> HTTP Response: %d" %responseCode)
        
        # wait some time to read again sensor values
        time.sleep(timeIntervall)
    
    except IOError:
        print ("Error")