require 'filewatcher'

# TODO: define the directory to watch
directory_to_watch = File.expand_path('../wav/sample_audio', __dir__)

Filewatcher.new([directory_to_watch], wait_for_delay: 1).watch do |changes|
  changes.each do |filename, event|
    puts "#{filename} #{event}"

    # Trigger the appropriate rake task based on the event
    case event
    when :created
      system("bundle exec rake audio_records:create[#{filename}]")
    when :updated
      system("bundle exec rake audio_records:update[#{filename}]")
    when :deleted
      system("bundle exec rake audio_records:delete[#{filename}]")
    end
  end
end
