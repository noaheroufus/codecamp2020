from inventory_item import InventoryItem

class Dish(InventoryItem):
    def __init__(self, name="ItemDish", size=(16,16), weight=0, graphic=False):
        super().__init__(name, size, weight, graphic)
    
    def action(self, player):
        pass