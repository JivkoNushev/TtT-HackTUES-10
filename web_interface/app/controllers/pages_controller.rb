class PagesController < ApplicationController
  def home
    @pagy, @audios = pagy(Audio.all.order(created_at: :desc))
    @equipment = Equipment.all
  end
end
