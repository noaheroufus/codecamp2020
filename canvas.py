import pygame

class Canvas:
    game = False
    surface = False

    def __init__(self, game):
        self.game = game
        self.surface = pygame.Surface(self.game.screen_size)
    
    def render(self, objects):
        self.surface.fill((100,100,100))
        for obj in objects:
            obj.render()
        scaled = pygame.transform.scale(self.surface, self.game.screen.get_size())
        self.game.screen.blit(scaled, (0,0))