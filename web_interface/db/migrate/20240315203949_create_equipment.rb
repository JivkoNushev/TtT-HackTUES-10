class CreateEquipment < ActiveRecord::Migration[7.1]
  def change
    create_table :equipment do |t|
      t.string :name
      t.integer :status

      t.timestamps
    end
  end
end
