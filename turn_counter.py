import pygame
from event import Event

class TurnCounter():
    TURN_PLAYER = 0
    TURN_ENEMY = 1

    MACHINE_TURN_COUNTER = 0

    def __init__(self, turn_list=[TURN_PLAYER, TURN_ENEMY]):
        self.turn_list = turn_list
        self.turn_index = 0
        self.turn_number = 0;

    def get_turn(self):
        return self.turn_list[self.turn_index]
    def is_player_turn(self):
        return self.get_turn() == self.TURN_PLAYER

    def turn_advance(self):
        self.turn_index += 1
        if self.turn_index >= len(self.turn_list):
            self.turn_index = 0
            self.turn_number += 1
            pygame.event.post(pygame.event.Event(Event.EVENT_RESET, machine=self.MACHINE_TURN_COUNTER))
