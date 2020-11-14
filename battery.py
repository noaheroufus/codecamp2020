from inventory_item import InventoryItem

class Battery(InventoryItem):
    def __init__(self, name="ItemBattery", size=(16,16), weight=0, graphic=False):
        super().__init__(name, size, weight, graphic)