import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'Indiana'
password = 'mitko123'
mqtt_server = '192.168.43.140'
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'noise'

SAMPLE_RATE = 44100
# SAMPLE_RATE_IN_HZ = 1
SAMPLE_WIDTH = 1 << 16 - 1
NUM_SAMPLE_BYTES_TO_WRITE = 1000
negative = -1

def connect_and_subscribe_to_mqtt():
  global client_id, mqtt_server, topic_pub
  client = MQTTClient(client_id, mqtt_server)
  client.connect()
  print('Connected to %s MQTT broker' % (mqtt_server))
  return client

def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

def connect_to_wifi():
  station = network.WLAN(network.STA_IF)

  station.active(True)
  station.connect(ssid, password)

  while station.isconnected() == False:
    pass

  print('Connection successful')
  print(station.ifconfig())

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    valueScaled = (value * rightSpan) // leftSpan

    return valueScaled

pot = machine.ADC(machine.Pin(36))
pot.atten(machine.ADC.ATTN_11DB)

try:
  connect_to_wifi()
  client = connect_and_subscribe_to_mqtt()
except OSError as e:
  restart_and_reconnect()

analog_values = []
interval = 5
last_read = 0

while True:
  try:
    if time.time() - last_read > interval:
      analog_values = []
      for i in range(NUM_SAMPLE_BYTES_TO_WRITE):
        msg = pot.read()
        print(msg)
        if msg > 0:
          if i == 0:
              timestamp = time.gmtime()
              analog_values.append(timestamp)
          msg = translate(msg, 0, 4095, -32768, 32767)
          analog_values.append(msg)
          # time.sleep(1 / SAMPLE_RATE)
      print(analog_values)
      client.publish(topic_pub, str(analog_values), 0)
      last_read = time.time()
  except OSError as e:
    restart_and_reconnect()