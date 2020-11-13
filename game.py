import sys,pygame
from graphics import Graphics

class Game:
    screenSize = screenWidth, screenHeight = 320, 240
    screen = 0
    running = False

    def __init__(self):
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.init()
        self.graphics = Graphics()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def render(self):
        self.screen.fill((100,100,100))
        self.screen.blit(self.graphics.player, (self.screenWidth/2, self.screenHeight/2))
        pygame.display.flip()

    def loop(self):
        self.running = True
        while self.running:
            self.update()
            self.render()
        
        sys.exit()
