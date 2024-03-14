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
topic_pub = 'silence'

last_message = 0
message_interval = 5

def message_handling(topic, msg):
    print(topic +": " + msg)

def connect_and_subscribe_to_mqtt():
  global client_id, mqtt_server, topic_pub
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(message_handling)
  client.connect()
  client.subscribe(topic_pub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_pub))
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


try:
  connect_to_wifi()
  client = connect_and_subscribe_to_mqtt()
except OSError as e:
  restart_and_reconnect()

while True:
  try:
    client.check_msg()
  except OSError as e:
    restart_and_reconnect()
