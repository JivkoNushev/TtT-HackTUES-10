task :read_audio_records => :environment do
  audio_files = Dir.glob("#{Audio.audio_folder_path}/*.wav")
  audio_files.each do |file|
    filename = File.basename(file)

    # Check if an audio record with the same filename already exists
    next if Audio.joins(audio_file_attachment: :blob)
                  .where(active_storage_blobs: { filename: filename })
                  .exists?

    audio = Audio.create(audio_file: File.open(file))
    puts "Created audio record for #{filename}" if audio.persisted?
  end
end

task db_seed: :read_audio_records