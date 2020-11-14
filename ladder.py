from object import Object
from rung import Rung

class Ladder(Object):
    def __init__(self, game, width, height, position):
        super().__init__(game, position)
        self.width = width
        self.height = height
        self.cells = []   # [x][y]
        for i in range(height):
            self.cells.append([]) # Append Row
            for j in range(width-2):
                # Add item in cell
                self.cells[i].append(Rung(game, ((j*self.game.sprite_width)+self.game.sprite_width, i*self.game.sprite_width)))

    def render(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                #print("Rendering cell at", j, ",", i)
                self.cells[i][j].render()
