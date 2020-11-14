import pygame

class InventoryItem:
    size = (10,10)
    name = ""
    weight = 0
    graphic = False

    def __init__(self, name="GenericItem", size=(10,10), weight=0, graphic=False):
        self.name = name
        self.size = size
        self.weight = weight
        self.graphic = graphic

    def get_name(self):
        return self.name
    
    def get_weight(self):
        return self.weight
    
    def render(self, game, position):
        surface = False
        if game.player.graphic:
            surface = game.player.graphic.graphics[game.player.graphic.position]

        if self.graphic and surface:
            scaled = pygame.transform.scale(self.graphic.graphics[0], self.size)
            surface.blit(scaled, (16,8))
        else:
            rect = pygame.Surface(self.size)
            rect.fill((255,255,255))
            game.player.graphic.graphics[game.player.graphic.position].blit(rect, (0,0))