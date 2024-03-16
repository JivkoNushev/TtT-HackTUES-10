require 'mqtt'

# Subscribe example
# 192.168.43.140:1883 - mosquitto broker from mitkos laptop

# MQTT::Client.connect('192.168.43.140', 1883) do |c|
MQTT::Client.connect(
  :host => "mqtt-dashboard.com",
  :port => 8884
) do |client|

  puts client
  topic = "tues/testtopic/1"
  payload = { test: "This test message."}.to_json
  client.publish(topic, payload, retain=false, qos=1)

end

# client.subscribe("tues/testtopic/1")

# # To receive a message from a topic:
# client.get do |topic, message|
#     puts "#{topic}: #{message}"
# end
