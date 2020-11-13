import pygame

class Object:
    game = False
    size = (0, 0)
    position = (0, 0)
    velocity = (0, 0)
    graphic = False

    def __init__(self, game, position, size, graphic=False):
        self.game = game
        self.position = position
        self.size = size
        self.graphic = graphic

    def set_velocity(self, x, y):
        self.velocity = (x, y)

    def update(self):
        self.position = (
            self.position[0]+self.velocity[0],
            self.position[1]+self.velocity[1]
        )
    
    def render(self):
        if self.graphic:
            self.graphic.render(self.game.screen, self.position)
        else:
            pygame.draw.rect(self.game.screen, (255,255,255), pygame.Rect(
                self.position[0], self.position[1],
                self.position[0]+self.size[0], self.position[1]+self.size[1],
            ))
