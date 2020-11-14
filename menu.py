from object import Object
import pygame

# Stores a background image and is able to switch between multiple options and select one
class Menu(Object):
    def __init__(self, game, position, options, pointer=False):
        super().__init__(game, position)
        self.options = options
        self.selection = 0
        self.pointer = pointer
        self.height = int(len(self.options)/2)
        if self.height < len(self.options)/2:
            self.height += 1
        self.width = 3

    def handle_event(self, event):
        if event.key == pygame.K_DOWN:
            self.selection += 1
            if self.selection >= len(self.options):
                self.selection = len(self.options)-1
        if event.key == pygame.K_UP:
            self.selection -= 1
            if self.selection < 0:
                self.selection = 0

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                cell = self.game.graphics.menu_c
                if i == 0 and j == 0: cell = self.game.graphics.menu_sw
                elif i == 0 and j > 0 and j < self.width-1: cell = self.game.graphics.menu_s
                elif i == 0 and j == self.width-1: cell = self.game.graphics.menu_se
                elif i > 0 and i < self.height-1 and j == 0: cell = self.game.graphics.menu_w
                elif i == self.height-1 and j == 0: cell = self.game.graphics.menu_nw
                elif i == self.height-1 and j > 0 and j < self.width-1: cell = self.game.graphics.menu_n
                elif i == self.height-1 and j == self.width-1: cell = self.game.graphics.menu_ne
                elif i > 0 and i < self.height-1 and j == self.width-1: cell = self.game.graphics.menu_e
                self.game.canvas.surface.blit(cell, (self.position[0]+(self.game.sprite_width*j), self.position[1]-(self.game.sprite_height*(i+1))))
        if self.pointer:
            self.pointer.render(self.game.canvas.surface, (self.position[0], self.position[1]-(self.game.sprite_height*self.height)+(self.game.sprite_height/2*self.selection)))
