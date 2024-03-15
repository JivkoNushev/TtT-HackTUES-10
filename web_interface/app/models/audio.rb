class Audio < ApplicationRecord
  has_one_attached :audio_file

  def self.audio_folder_path
    # TODO: change when adding to the raspberry pi
    Rails.root.join('..', 'wav', 'sample_audio')
  end
end