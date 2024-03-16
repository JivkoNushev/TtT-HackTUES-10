class Audio < ApplicationRecord

  after_create_commit -> {
    broadcast_prepend_to "audios", target: "audios", partial: "audios/audio", locals: { audio: self }
  }

  has_one_attached :audio_file

  def self.audio_folder_path
    # TODO: change when adding to the raspberry pi
    Rails.root.join('..', 'wav', 'sample_audio')
  end
end