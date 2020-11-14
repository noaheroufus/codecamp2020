import pygame
from object import Object
from event import Event
from inventory import Inventory
from wrench import Wrench
from graphic import Graphic

class Player(Object):
    inventory = False
    health = 100
    armour = 100

    def __init__(self, game, position, size, graphic=False):
        super().__init__(game, position, size, graphic)
        self.hanging = False

        self.inventory = Inventory(100)
        self.inventory.add_item(Wrench(weight=10, graphic=Graphic([graphics.wrench], [0])))
        
        self.previous_rung = (int(position[0]/game.sprite_width), int(position[1]/game.sprite_height))

    def update(self):
        super().update()
        # if colliding with rung


    def render(self):
        super().render()

        item = self.inventory.get_active_item()
        if item:
            item.render(self.game, self.position)

    def move(self):
        if self.hanging:
            # Move
            print("Should move")
    def handle_event(self, event):
        if event.type == Event.EVENT_KEY_PRESSED:
            if event.key == pygame.K_RIGHT:
                self.jump_right()
            if event.key == pygame.K_DOWN:
                self.jump_down()
            if event.key == pygame.K_LEFT:
                self.jump_left()
            if event.key == pygame.K_UP:
                self.jump_up()
            if event.key == pygame.K_SPACE:
                self.start_climbing()
            
    def get_health(self):
        return self.health

    def set_health(self, health):
        if health > 100:
            self.health = 100
        elif health < 0:
            self.health = 0
        else:
            self.health = health

    def get_armour(self):
        return self.armour

    def set_armour(self, armour):
        if armour > 100:
            self.armour = 100
        elif armour < 0:
            self.armour = 0
        else:
            self.armour = armour

    def start_climbing(self):
        self.graphic.graphics = [self.game.graphics.player_hang]
        self.graphic.times = [1]
    def jump_down(self):
        self.graphic.graphics = [self.game.graphics.player_hang]
        self.graphic.times = [1]
        self.set_velocity(0, 1)
    def jump_up(self):
        self.graphic.graphics = [self.game.graphics.player_hang_jump]
        self.graphic.times = [1]
        self.set_velocity(0, -1)
    def jump_left(self):
        self.graphic.graphics = [self.game.graphics.player_hang_jump_left]
        self.graphic.times = [1]
        self.set_velocity(-1, 0)
    def jump_right(self):
        self.graphic.graphics = [self.game.graphics.player_hang_jump_right]
        self.graphic.times = [1]
        self.set_velocity(1, 0)
