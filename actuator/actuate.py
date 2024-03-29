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

client.subscribe("silence")

try:
    print("Press CTRL+C to exit...")
    client.loop_start()
    topic = "active/speaker"
    while True:
        status = 5 # in_operation
        for i in range(0,3):
          client.publish(topic, status, 0)
          print(f"Speaker is with status {status}")
          time.sleep(random.randint(5, 10))

        status = 1 # calibration_required
        client.publish(topic, status, 0)
        print(f"Speaker is with status {status}")
        time.sleep(random.randint(9, 11))

except Exception:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()