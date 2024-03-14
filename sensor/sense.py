import sys
import time
import paho.mqtt.client as paho

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

SAMPLE_RATE = 44100
# SAMPLE_RATE_IN_HZ = 1
SAMPLE_WIDTH = 1 << 16 - 1
NUM_SAMPLE_BYTES_TO_WRITE = 10
negative = -1

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    valueScaled = (value * rightSpan) // leftSpan

    return valueScaled

analog_values = []
analog_values_inverted = []

for i in range(NUM_SAMPLE_BYTES_TO_WRITE):
    value = (i % SAMPLE_WIDTH)
    if value > 0:
        if i == 0:
            timestamp = time.time
            analog_values.append(timestamp)
        value = translate(value, 0, 4095, 0, 65535)
        analog_values.append(value)
    time.sleep(1 / SAMPLE_RATE)

print(analog_values)
client.publish("noise", str(analog_values), 0)
client.disconnect()