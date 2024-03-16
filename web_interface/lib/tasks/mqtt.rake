# lib/tasks/mqtt.rake

namespace :mqtt do
  desc "Handle incoming mqtt traffic"
  task :handle, [:name, :status] => :environment do |t, args|
    name = args[:name].split("/").last.capitalize
    status = args[:status].to_i
    puts "Name: #{name}"
    puts "Status: #{Equipment.statuses.key(status)}"

    equipment = Equipment.find_by(name: name)
    if equipment
      if equipment.status != Equipment.statuses.key(status)
        equipment.update(status: status)
        puts "Equipment updated"
      end
    else
      Equipment.create(name: name, status: status)
      puts "Equipment created"
    end
  end
end