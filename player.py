from object import Object
from event import Event
from inventory import Inventory

class Player(Object):
    inventory = False
    health = 100
    armour = 100

    def __init__(self, game, position, size, graphic=False):
        super().__init__(game, position, size, graphic)
        self.hanging = False

        self.inventory = Inventory(100)

    def update(self):
        super().update()
        # if colliding with rung

    def render(self):
        super().render()

        item = self.inventory.get_active_item()
        if item:
            item.render(self.game, self.position)

    def move(self):
        if self.hanging:
            # Move
            Print("Should move")
    def handle_event(self, event):
        if event.type == Event.EVENT_PLAYER_MOVE_RIGHT:
            self.set_velocity(1, 0)
        if event.type == Event.EVENT_PLAYER_MOVE_DOWN:
            self.set_velocity(0, 1)
        if event.type == Event.EVENT_PLAYER_MOVE_LEFT:
            self.set_velocity(-1, 0)
        if event.type == Event.EVENT_PLAYER_MOVE_UP:
            self.set_velocity(0, -1)
        if event.type == Event.EVENT_SPACE:
            self.start_climbing()
            
    def get_health(self):
        return self.health

    def set_health(self, health):
        if health > 100:
            self.health = 100
        elif health < 0:
            self.health = 0
        else:
            self.health = health

    def get_armour(self):
        return self.armour

    def set_armour(self, armour):
        if armour > 100:
            self.armour = 100
        elif armour < 0:
            self.armour = 0
        else:
            self.armour = armour

    def start_climbing(self):
        self.graphic.graphics = [self.game.graphics.player_hang]
        self.graphic.times = [1]
