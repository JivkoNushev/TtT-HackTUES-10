import sys
import time
import paho.mqtt.client as paho
import random

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = paho.Client()
client.on_message = message_handling

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

try:
    print("Press CTRL+C to exit...")
    client.loop_start()
    topic = "active/microphone"
    while True:
        status = 5 # in_operation
        for i in range(0,2):
          client.publish(topic, status, 0)
          print(f"Microphone is with status {status}")
          time.sleep(random.randint(8, 11))

        status = 4 # ready
        client.publish(topic, status, 0)
        print(f"Microphone is with status {status}")
        time.sleep(random.randint(4,6))

except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()