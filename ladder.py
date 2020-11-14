from object import Object
from rung import *
import random

class Ladder(Object):
    def __init__(self, game, width, height, position):
        super().__init__(game, position)
        self.width = width
        self.height = height
        self.cells = []   # [x][y]
        cell_options = [
            Rung,
            RungFrozen,
            RungPacket,
            RungUpgradeStation
        ]
        cell_weights = [.919, .06, .02, .001]
        cell_blob = random.choices(cell_options, cell_weights, k=height*(width-2))
        iterator = 0
        for i in range(height):
            self.cells.append([]) # Append Row
            for j in range(width-2):
                # Add item in cell
                self.cells[i].append(cell_blob[iterator](game, ((j*self.game.sprite_width)+self.game.sprite_width, i*self.game.sprite_width)))
                iterator += 1

    def render(self):
        for i in range(len(self.cells)):
            for j in range(len(self.cells[i])):
                #print("Rendering cell at", j, ",", i)
                self.cells[i][j].render()

    def convert_to_ladder_coords(self, position):
        ladder_x = int(position[0]/self.game.sprite_width)-1
        ladder_y = int(position[1]/self.game.sprite_height)
        return (ladder_x, ladder_y)
    def in_range(self, coords):
        return coords[1] >= 0 and coords[1] < len(self.cells) and coords[0] >= 0 and coords[0] < len(self.cells[coords[1]])
