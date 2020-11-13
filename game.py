import sys,pygame

class game:
    screenSize = screenWidth, screenHeight = 320, 240
    screen = 0
    running = False

    def __init__(self):
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.init()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def render(self):
        self.screen.fill((0,0,0))
        pygame.display.flip()

    def loop(self):
        self.running = True
        while self.running:
            self.update()
            self.render()
        
        sys.exit()
