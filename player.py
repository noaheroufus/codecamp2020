from object import Object
from event import Event
from state import State

class Player(Object):

    health = 100
    armour = 100

    def __init__(self, game, position, size, graphic=False):
        super().__init__(game, position, size, graphic)

    def update(self):
        super().update()

    def render(self):
        super().render()

    def handle_event(self, event):
        if self.game.state.get_state() == State.STATE_GAME_CLIMB:
            if event.type == Event.EVENT_PLAYER_MOVE_RIGHT:
                if self.game.timer.ready():
                    self.set_velocity(1, 0)
            if event.type == Event.EVENT_PLAYER_MOVE_DOWN:
                if self.game.timer.ready():
                    self.set_velocity(0, 1)
            if event.type == Event.EVENT_PLAYER_MOVE_LEFT:
                if self.game.timer.ready():
                    self.set_velocity(-1, 0)
            if event.type == Event.EVENT_PLAYER_MOVE_UP:
                if self.game.timer.ready():
                    self.set_velocity(0, -1)
            
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


