import os, pygame

class Graphics:
    def __init__(self):
        self.load_images()
    def load_images(self):
        self.player = pygame.image.load(os.path.join('graphics', 'player_idle.png')).convert_alpha()
