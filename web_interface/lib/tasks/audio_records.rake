# lib/tasks/audio_records.rake

namespace :audio_records do
  desc "Create audio record"
  task :create, [:filename] => :environment do |t, args|
    filename = args[:filename]

    # Attempt to create the audio record
    audio = Audio.create(audio_file: File.open(filename))

    if audio.persisted?
      puts "Successfully created audio record for #{filename}"
    else
      puts "Failed to create audio record for #{filename}"
    end
  end

  # NOTE: not done
  # desc "Update audio record"
  # task :update, [:filename] => :environment do |t, args|
  #   filename = args[:filename]
  #   # Your logic for updating the audio record associated with the provided filename
  #   puts "Updating audio record for #{filename}..."
  # end

  ## NOTE: not done
  # desc "Delete audio record"
  # task :delete, [:filename] => :environment do |t, args|
  #   filename = args[:filename]

  #   # Find the audio record with the provided filename
  #   audio = Audio.joins(audio_file_attachment: :blob)
  #         .where(active_storage_blobs: { filename: filename })
  #         .first
  #  # when testing in the console audio.present? returns true, but in the rake task it returns false
  #   if audio.present?
  #     # Delete the audio record if found
  #     audio.destroy
  #     puts "Successfully deleted audio record for #{filename}"
  #   else
  #     puts "Audio record for #{filename} not found"
  #   end
  # end

  desc "Read all files"
  task :read_all => :environment do
    audio_files = Dir.glob("#{Audio.audio_folder_path}/*.wav")
    audio_files.each do |file|
      filename = File.basename(file)

      # Check if an audio record with the same filename already exists
      next if Audio.joins(audio_file_attachment: :blob)
                    .where(active_storage_blobs: { filename: filename })
                    .exists?

      # Create an Audio record
      audio = Audio.create(audio_file: File.open(file))
      puts "Created audio record for #{filename}"

      ## Delete files from the system when it is loaded in the database:
      # if audio.persisted?
      #   # Delete the file from the system after processing
      #   File.delete(file)
      #   puts "Deleted file #{filename} from the system"
      # else
      #   puts "Failed to create audio record for #{filename}"
      # end
    end
  end

  task db_seed: :read_all
end