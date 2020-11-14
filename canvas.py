import pygame
from state import State

class Canvas:
    game = False
    surface = False
    transitioning = False
    transition_surface = False
    transition_toggle = False
    transition_new_state = False

    def __init__(self, game):
        self.game = game
        self.surface = pygame.Surface(self.game.screen_size)

    def transition(self, new_state):
        self.transition_new_state = new_state
        self.transitioning = True
        self.transition_surface = pygame.Surface(self.game.screen.get_size())
        self.transition_surface.fill((0,0,0))
        self.transition_surface.set_alpha(0)

    def render(self):
        self.surface.fill((100,100,100))
        if self.game.state.get_state() == State.STATE_GAME_MENU:
            self.surface.fill((100,100,100))
            ## TODO: Add menu text
        for obj in self.game.game_objects[self.game.state.get_state()]:
            obj.render()
        scaled = pygame.transform.scale(self.surface, self.game.screen.get_size())
        self.game.screen.blit(scaled, (0,0))

        if self.transitioning:
            if self.transition_toggle:
                if self.transition_surface.get_alpha() > 0:
                    self.transition_surface.set_alpha(self.transition_surface.get_alpha()-5)
                else:
                    self.transitioning = False
                    self.transition_toggle = False
            else:
                if self.transition_surface.get_alpha() < 255:
                    self.transition_surface.set_alpha(self.transition_surface.get_alpha()+5)
                else:
                    self.game.state.set_state(self.transition_new_state)
                    self.transition_toggle = True
            self.game.screen.blit(self.transition_surface, (0,0))
