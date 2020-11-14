from object import Object
from graphic import Graphic

class Rung(Object):
    def __init__(self, game, position, graphic=False):
        g = graphic
        if not g:
            g = Graphic([game.graphics.rung],[0])
        super().__init__(game, position, graphic=g)

class RungFrozen(Rung):
    def __init__(self, game, position):
        super().__init__(game, position, Graphic([game.graphics.rung_frozen],[0]))

class RungPacket(Rung):
    def __init__(self, game, position):
        super().__init__(game, position, Graphic([game.graphics.rung_packet],[0]))
        self.collected = False
    def collect(self):
        self.collected = True
        self.graphic = Graphic([self.game.graphics.rung],[0])

class RungUpgradeStation(Rung):
    def __init__(self, game, position):
        super().__init__(game, position, Graphic([game.graphics.rung_upgrade_station],[0]))
