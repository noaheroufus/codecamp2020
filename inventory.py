from inventory_item import InventoryItem

class Inventory:
    max_weight = -1
    items = []
    active_item = -1

    def __init__(self, max_weight):
        self.max_weight = max_weight
    
    def add_item(self, item):
        for i in self.items:
            if item.get_name() == i.get_name():
                i.quantity += 1
                return

        if (self.get_weight() + item.weight) <= self.max_weight:
            self.items.append(item)
    
    def get_items(self):
        return self.items
    def get_num_items(self, item):
        for i in self.get_items():
            if i.get_name() == item:
                return i.get_quantity()
        return 0

    def get_active_item(self):
        if len(self.items) > 0:
            if self.active_item < 0:
                self.active_item = 0
            
            return self.items[self.active_item]
        else:
            return False

    def swap(self):
        if self.active_item+1 < len(self.items):
            self.active_item+=1
        else:
            self.active_item=0
    
    def action(self, player):
        self.get_active_item().action(player)

    def get_weight(self):
        weight = 0
        for item in self.items:
            weight += item.weight
        
        return weight
