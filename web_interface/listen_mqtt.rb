require 'mqtt'

MQTT::Client.connect(
  :host => "localhost",
  :port => 1883
) do |client|

  topic = "active/#"

  client.subscribe(topic)

  client.get do |topic, message|
    system("bundle exec rake mqtt:handle[\"#{topic}\",\"#{message}\"]")
  end
end

