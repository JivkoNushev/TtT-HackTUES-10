require 'mqtt'

# Subscribe example
# 192.168.43.140:1883 - mosquitto broker from mitkos laptop

# MQTT::Client.connect('192.168.43.140', 1883) do |c|
client = MQTT::Client.connect(:host => "mqtt-dashboard.com", :port => 8884 )

client.subscribe("tues/testtopic/1")

# To receive a message from a topic:
client.get do |topic, message|
    puts "#{topic}: #{message}"
end
