from object import Object
from graphic import Graphic

class Rung(Object):
    def __init__(self, game, position):
        super().__init__(game, position, graphic=Graphic([game.graphics.rung],[0]))
