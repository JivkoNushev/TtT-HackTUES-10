class AudiosController < ApplicationController
  def index
    @pagy, @audios = pagy(Audio.all.order(created_at: :desc), items: 20)
  end

  def show
    @audio = Audio.find(params[:id])
  end
end