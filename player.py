from object import Object
from event import Event
from inventory import Inventory

class Player(Object):
    inventory = False

    def __init__(self, game, position, size, graphic=False):
        super().__init__(game, position, size, graphic)

        self.inventory = Inventory(100)

    def update(self):
        super().update()

    def render(self):
        super().render()

        item = self.inventory.get_active_item()
        if item:
            item.render(self.game, self.position)

    def handle_event(self, event):
        if event.type == Event.EVENT_PLAYER_MOVE_RIGHT:
            self.set_velocity(1, 0)
        if event.type == Event.EVENT_PLAYER_MOVE_DOWN:
            self.set_velocity(0, 1)
        if event.type == Event.EVENT_PLAYER_MOVE_LEFT:
            self.set_velocity(-1, 0)
        if event.type == Event.EVENT_PLAYER_MOVE_UP:
            self.set_velocity(0, -1)
