import sys, pygame
from graphics import Graphics
pygame.init()

screenSize = screenWidth, screenHeight = 320, 240
screen = pygame.display.set_mode(screenSize)
black = (0, 0, 0)

playing = True

graphics = Graphics()

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    screen.blit(graphics.player, (screenWidth/2, screenHeight/2))
    pygame.display.flip()
