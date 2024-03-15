class AudiosController < ApplicationController
  def index
    @audios = Audio.all
  end

  def show
    @audio = Audio.find(params[:id])
  end
end