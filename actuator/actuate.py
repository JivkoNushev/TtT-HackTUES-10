import sys
import time
import paho.mqtt.client as paho


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
    while True:
        client.publish("active/speaker", 2, 0)
        time.sleep(5)

except Exception:
    print("Caught an Exception, something went wrong...")

finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()
