import pygame
from object import Object
from event import Event
from inventory import Inventory
from wrench import Wrench
from battery import Battery
from jammer import Jammer
from dish import Dish
from graphic import Graphic

class Player(Object):
    inventory = False
    health = 100
    armour = 100

    def __init__(self, game, position, size, graphic=False):
        super().__init__(game, position, size, graphic)
        self.hanging = False

        self.collision_radius = size[0]/10

        self.inventory = Inventory(100)
        self.inventory.add_item(Wrench(weight=10, graphic=Graphic([game.graphics.wrench], [0])))
        self.inventory.add_item(Battery(weight=10, graphic=Graphic([game.graphics.battery], [0])))
        self.inventory.add_item(Jammer(weight=10, graphic=Graphic([game.graphics.jammer], [0])))
        self.inventory.add_item(Dish(weight=10, graphic=Graphic([game.graphics.dish], [0])))
        
        self.previous_rung = (0,0)

    def update(self):
        super().update()
        # if colliding with rung
        ladder_coords = self.game.ladder.convert_to_ladder_coords(self.position)
        if self.game.ladder.in_range(ladder_coords) and ladder_coords != self.previous_rung:
            if (self.colliding(self.game.ladder.cells[ladder_coords[1]][ladder_coords[0]], self.collision_radius)):
                self.velocity = [0,0]
                self.previous_rung = ladder_coords
                self.hanging = True
                self.hang()

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
            if self.hanging:
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
        if event.type == Event.EVENT_CHANGE_ITEM:
            self.inventory.swap()
        if event.type == Event.EVENT_USE_ITEM:
            self.inventory.action(self)
            
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
        self.hang;
    def hang(self):
        self.graphic.graphics = [self.game.graphics.player_hang]
        self.graphic.times = [1]

    def jump_down(self):
        self.graphic.graphics = [self.game.graphics.player_hang]
        self.graphic.times = [1]
        self.set_velocity(0, 1)
        self.hanging = False
    def jump_up(self):
        self.graphic.graphics = [self.game.graphics.player_hang_jump]
        self.graphic.times = [1]
        self.set_velocity(0, -1)
        self.hanging = False
    def jump_left(self):
        self.graphic.graphics = [self.game.graphics.player_hang_jump_left]
        self.graphic.times = [1]
        self.set_velocity(-1, 0)
        self.hanging = False
    def jump_right(self):
        self.graphic.graphics = [self.game.graphics.player_hang_jump_right]
        self.graphic.times = [1]
        self.set_velocity(1, 0)
        self.hanging = False
