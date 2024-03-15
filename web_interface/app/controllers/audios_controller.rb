class AudiosController < ApplicationController
  def index
    @audios = Audio.all
  end

  def create
    audio_files = Dir.glob("#{Audio.audio_folder_path}/*.wav")

    audio_files.each do |file|
      audio = Audio.new
      audio.audio_file.attach(io: File.open(file), filename: File.basename(file))
      audio.save
    end

    redirect_to root_path, notice: 'Audio files uploaded successfully.'
  end
end