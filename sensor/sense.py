import sys

import paho.mqtt.client as paho

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.publish("noise", "Indiana Mitko", 0)
client.disconnect()