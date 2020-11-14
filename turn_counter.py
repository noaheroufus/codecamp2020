import pygame
from event import Event
from state import State

class TurnCounter():
    TURN_PLAYER = 0
    TURN_ENEMY = 1

    MACHINE_TURN_COUNTER = 0

    def __init__(self, turn_list=[TURN_PLAYER, TURN_ENEMY]):
        self.turn_list = turn_list
        self.turn_index = 0
        self.turn_number = 0;
        self.enemies = []

    def get_turn(self):
        return self.turn_list[self.turn_index]
    def is_player_turn(self):
        return self.get_turn() == self.TURN_PLAYER

    def turn_advance(self):
        self.turn_index += 1
        if len(self.enemies) > 0:
            print(self.enemies[0].health, "heart", self.enemies[0].armour, "armour")
            if not self.enemies[0].alive:
                self.enemies.pop(0)
                self.turn_advance()
        if self.turn_index >= len(self.turn_list):
            self.turn_index = 0
            self.turn_number += 1
            if len(self.enemies) <= 0:
                pygame.event.post(pygame.event.Event(Event.EVENT_CHANGE_STATE, state=State.STATE_GAME_CLIMB))
                return
            pygame.event.post(pygame.event.Event(Event.EVENT_RESET, machine=self.MACHINE_TURN_COUNTER))
        if self.turn_list[self.turn_index] == self.TURN_ENEMY:
            if len(self.enemies) > 0: self.enemies[0].act()

    def update(self): pass
    def render(self):
        for e in self.enemies:
            e.render()
