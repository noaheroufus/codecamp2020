from object import Object
from event import Event

class Player(Object):
    def __init__(self, game, position, size, graphic=False):
        super().__init__(game, position, size, graphic)

    def update(self):
        super().update()

    def render(self):
        super().render()

    def handle_event(self, event):
        if event.type == Event.EVENT_PLAYER_MOVE_RIGHT:
            self.set_velocity(1, 1)