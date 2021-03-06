import pygame, math
from object import Object
from event import Event
from inventory import Inventory
from wrench import Wrench
from battery import Battery
from jammer import Jammer
from dish import Dish
from graphic import Graphic
from state import State
from turn_counter import TurnCounter
from rung import *
from packet import Packet

class Player(Object):
    inventory = False
    health = 100
    hearts = 10
    max_hearts = 10
    armour = 100
    floor = 1

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

        self.defending = False
        self.jamming = False

    def update(self):
        super().update()

        self.hearts = math.ceil(self.health/20)
        if self.hearts > 5: self.hearts = 5
        if self.hearts < 1: self.hearts = 1

        if self.get_health() < 1:
            self.floor = 1
            self.hearts = 0
            pygame.event.post(pygame.event.Event(Event.EVENT_CHANGE_STATE, state=State.STATE_GAME_OVER))
        
        if self.game.state.get_state() == State.STATE_GAME_CLIMB:
            # if colliding with rung
            ladder_coords = self.game.ladder.convert_to_ladder_coords(self.position)
            if self.game.ladder.in_range(ladder_coords) and ladder_coords != self.previous_rung:
                rung = self.game.ladder.cells[ladder_coords[1]][ladder_coords[0]]
                if (self.colliding(rung, self.collision_radius)):
                    if type(rung) == RungPacket:
                        rung.collect()
                        self.inventory.add_item(Packet(("ItemPacket", (16,16), 0, Graphic([self.game.graphics.packet], [0]))))
                    if type(rung) == RungFrozen:
                        if self.game.action_timer.bg.graphics[0] != self.game.graphics.timer_face_hard:
                            self.game.action_timer.bg.graphics[0] = self.game.graphics.timer_face_hard
                    else:
                        if self.game.action_timer.bg.graphics[0] != self.game.graphics.timer_face:
                            self.game.action_timer.bg.graphics[0] = self.game.graphics.timer_face
                    self.velocity = [0,0]
                    self.previous_rung = ladder_coords
                    self.hanging = True
                    self.hang()
            if self.position[0] >= self.game.screen_width - self.size[0] or self.position[0] <= 0 or self.position[1]>self.game.screen_height-self.size[1]:
                self.set_health(0)
            if self.position[1]<=0:
                pygame.event.post(pygame.event.Event(Event.EVENT_CHANGE_STATE, state=State.STATE_GAME_BATTLE))

    def render(self):
        super().render()

        item = self.inventory.get_active_item()
        if item:
            item.render(self.game, self.position)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.game.state.get_state() == State.STATE_GAME_CLIMB:
                if self.hanging:
                    if event.key == pygame.K_RIGHT:
                        self.jump_right()
                    if event.key == pygame.K_DOWN:
                        self.jump_down()
                    if event.key == pygame.K_LEFT:
                        self.jump_left()
                    if event.key == pygame.K_UP:
                        self.jump_up()
            elif self.game.state == State.STATE_GAME_BATTLE:
                if self.acting:
                    # Matching minigame the button presses here
                    pass
        if event.type == Event.EVENT_CHANGE_ITEM:
            self.inventory.swap()
        if event.type == Event.EVENT_USE_ITEM:
            self.inventory.action(self)
        if event.type == Event.EVENT_RESET:
            if event.machine == TurnCounter.MACHINE_TURN_COUNTER:
                self.defending = False
                self.jamming = False

            
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
        if self.defending: return self.armour * 2
        else: return self.armour

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
        pos = self.game.action_timer.needle.position
        rung = self.game.ladder.cells[self.previous_rung[1]][self.previous_rung[0]]
        if (type(rung) != RungFrozen and (pos == 0 or pos == 1 or pos == 7)) or (type(rung)==RungFrozen and pos == 1):
            self.graphic.graphics = [self.game.graphics.player_hang_jump]
            self.graphic.times = [1]
            self.set_velocity(0, -1)
            self.hanging = False
        else:
            self.jump_down()
    def jump_left(self):
        pos = self.game.action_timer.needle.position
        rung = self.game.ladder.cells[self.previous_rung[1]][self.previous_rung[0]]
        if (type(rung) != RungFrozen and (pos == 0 or pos == 1 or pos == 7)) or (type(rung)==RungFrozen and pos == 1):
            self.graphic.graphics = [self.game.graphics.player_hang_jump_left]
            self.graphic.times = [1]
            self.set_velocity(-1, 0)
            self.hanging = False
        else:
            self.jump_down()
    def jump_right(self):
        pos = self.game.action_timer.needle.position
        rung = self.game.ladder.cells[self.previous_rung[1]][self.previous_rung[0]]
        if (type(rung) != RungFrozen and (pos == 0 or pos == 1 or pos == 7)) or (type(rung)==RungFrozen and pos == 1):
            self.graphic.graphics = [self.game.graphics.player_hang_jump_right]
            self.graphic.times = [1]
            self.set_velocity(1, 0)
            self.hanging = False
        else:
            self.jump_down()
        self.graphic.graphics = [self.game.graphics.player_hang_jump_right]
        self.graphic.times = [1]
        self.set_velocity(1, 0)
        self.hanging = False

    def attack(self, other):
        other.damage(self.inventory.get_active_item().weight)
    def damage(self, weight):
        if self.armour > 0:
            new_armour = self.get_armour() - weight
            if self.armour > new_armour: self.armour = new_armour
        else:
            self.health -= weight
