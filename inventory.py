from inventory_item import InventoryItem

class Inventory:
    max_weight = -1
    items = []
    active_item = -1

    def __init__(self, max_weight):
        self.max_weight = max_weight
    
    def add_item(self, item):
        if (self.get_weight() + item.weight) <= self.max_weight:
            self.items.append(item)
    
    def get_items(self):
        return self.items

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

    def get_weight(self):
        weight = 0
        for item in self.items:
            weight += item.weight
        
        return weight