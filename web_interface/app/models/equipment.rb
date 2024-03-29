class Equipment < ApplicationRecord
  enum status: {
    maintenance_required: 0,
    calibration_required: 1,
    error: 2,

    initializing: 3,

    ready: 4,
    in_operation: 5
  }

  after_create_commit -> {
    broadcast_append_to "equipments", target: "equipments", partial: 'equipment/item', locals: { item: self }
  }

  after_update_commit -> {
    broadcast_replace_to "equipments", target: self, partial: "equipment/item", locals: { item: self }
  }
end
