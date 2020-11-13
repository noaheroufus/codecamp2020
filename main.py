import sys, pygame
pygame.init()

screenSize = screenWidth, screenHeight = 320, 240
screen = pygame.display.set_mode(screenSize)
black = (0, 0, 0)

playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)
    pygame.display.flip()
