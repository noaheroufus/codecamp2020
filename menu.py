from object import Object
import pygame

# Stores a background image and is able to switch between multiple options and select one
class Menu(Object):
    def __init__(self, game, position, options, size=(64,32), background=False, pointer=False):
        super().__init__(game, position, size, background)
        self.options = options
        self.selection = 0
        self.pointer = pointer

    def handle_event(self, event):
        if event.key == pygame.K_DOWN:
            self.selection += 1
            if self.selection >= len(self.options):
                self.selection = len(self.options)-1

    def render(self):
        super().render()
        if self.pointer:
            pass
