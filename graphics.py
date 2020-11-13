import os, pygame

class Graphics:
    def __init__(self):
        self.load_images()
    def load_images(self):
        self.player_idle = pygame.image.load(os.path.join('graphics', 'player_idle.png')).convert_alpha()
        self.player_walk_0 = pygame.image.load(os.path.join('graphics', 'player_walk_0.png')).convert_alpha()
        self.player_walk_1 = pygame.image.load(os.path.join('graphics', 'player_walk_1.png')).convert_alpha()
        self.player_walk_2 = pygame.image.load(os.path.join('graphics', 'player_walk_2.png')).convert_alpha()
