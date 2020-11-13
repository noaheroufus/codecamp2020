import os, pygame

class Graphics:
    def __init__(self):
        self.LoadImages()
    def LoadImages(self):
        self.player = pygame.image.load(os.path.join('graphics', 'player.png'))
