import pygame

class Object:
    game = False
    size = (0, 0)
    position = (0, 0)
    velocity = [0, 0]
    graphic = False

    def __init__(self, game, position, size=(32,32), graphic=False, color=(255,255,255)):
        self.game = game
        self.position = position
        self.graphic = graphic
        self.size = size
        self.color = color

    def set_velocity(self, x, y):
        self.velocity = [x, y]
    def set_velocity_x(self, x):
        self.velocity[0] = x
    def set_velocity_y(self, y):
        self.velocity[1] = y

    def update(self):
        self.position = (
            self.position[0]+self.velocity[0],
            self.position[1]+self.velocity[1]
        )
    
    def render(self):
        if self.graphic:
            scaled = pygame.transform.scale(self.graphic.graphics[0], self.size)
            self.game.canvas.surface.blit(scaled, self.position)
        else:
            rect = pygame.Surface(self.size)
            rect.fill(self.color)
            self.game.canvas.surface.blit(rect, self.position)

    def colliding(self, other, distance):
        dx = other.position[0] - self.position[0]
        dy = other.position[1] - self.position[1]
        return (dx * dx) + (dy * dy) <= distance * distance
