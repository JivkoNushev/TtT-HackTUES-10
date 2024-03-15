class Equipment < ApplicationRecord
  enum status: {
    maintenance_required: 0,
    calibration_required: 1,
    error: 2,

    initializing: 3,

    ready: 4,
    in_operation: 5
  }
end
