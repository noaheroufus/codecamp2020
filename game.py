import sys,pygame
from graphics import Graphics
from object import Object

class Game:
    screenSize = screenWidth, screenHeight = 320, 240
    screen = 0
    running = False
    objects = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.screenSize)
        self.graphics = Graphics()
        player = Object(self, (self.screenWidth/2, self.screenHeight/2), (32,32), self.graphics.player)
        self.objects.append(player)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
        for obj in self.objects:
            obj.update()
    
    def render(self):
        self.screen.fill((0,0,0))
        
        for obj in self.objects:
            obj.render()
      
        pygame.display.flip()

    def loop(self):
        self.running = True
        while self.running:
            self.update()
            self.render()
        
        sys.exit()
