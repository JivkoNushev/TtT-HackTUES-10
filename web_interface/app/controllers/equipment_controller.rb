class EquipmentController < ApplicationController
  def index
    @equipment = Equipment.all
  end

  def show
    @item = Equipment.find(params[:id])
  end
end
