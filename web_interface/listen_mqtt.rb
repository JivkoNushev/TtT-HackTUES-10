require 'mqtt'

MQTT::Client.connect(
  :host => "localhost",
  :port => 1883
) do |client|

  topic = "active/#"
  client.subscribe(topic)

  last_message_times = Hash.new(0)
  timeout_thread = Thread.new do
    loop do
      last_message_times.each do |topic, last_time|
        if Time.now.to_i - last_time >= 10
          system("bundle exec rake mqtt:collapse[\"#{topic}\"]")
        end
      end
      sleep 10
    end
  end

  client.get do |topic, message|
    last_message_times[topic] = Time.now.to_i
    system("bundle exec rake mqtt:handle[\"#{topic}\",\"#{message}\"]")
  end

  timeout_thread.join
end
