task :read_audio_records => :environment do
  audio_files = Dir.glob("#{Audio.audio_folder_path}/*.wav")
  audio_files.each do |file|
    audio = Audio.create(audio_file: File.open(file))
    puts "Created audio record for #{audio.audio_file.filename}" if audio.persisted?
  end
end

task db_seed: :read_audio_records