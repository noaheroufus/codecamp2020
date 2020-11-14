from object import Object
import pygame

class Text(Object):
    def __init__(self, game, position, text):
        super().__init__(game, position, (5,5))
        self.font = pygame.font.SysFont("Bungee Inline", int(game.sprite_height/2-(game.sprite_height/10)))
        self.text = text

    def render(self):
        self.game.canvas.surface.blit(self.font.render(self.text, False, (0,0,0)), self.position)
