import pygame
from state import State

class Canvas:
    game = False
    surface = False

    def __init__(self, game):
        self.game = game
        self.surface = pygame.Surface(self.game.screen_size)
    
    def render(self):
        if self.game.state.get_state() == State.STATE_GAME_MENU:
            self.surface.fill((100,100,100))
            ## TODO: Add menu text
        for obj in self.game.game_objects[self.game.state.get_state()]:
            obj.render()
        scaled = pygame.transform.scale(self.surface, self.game.screen.get_size())
        self.game.screen.blit(scaled, (0,0))
