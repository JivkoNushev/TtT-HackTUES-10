class PagesController < ApplicationController
  def home
    @pagy, @audios = pagy(Audio.all.order(created_at: :desc))
  end
end
