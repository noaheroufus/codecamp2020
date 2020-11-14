from object import Object
import pygame,os

class Text(Object):
    def __init__(self, game, position, text, size=False, color=(0,0,0)):
        super().__init__(game, position, (5,5))
        if not size:
            size = int(game.sprite_height/2-(game.sprite_height/10))
        self.font = pygame.font.Font(os.path.join('fonts', 'BungeeInline.ttf'), size)
        self.text = text
        self.color = color

    def render(self):
        self.game.canvas.surface.blit(self.font.render(self.text, False, self.color), self.position)
