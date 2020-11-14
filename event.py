import pygame

class Event:
    EVENT_PLAYER_MOVE_RIGHT = pygame.USEREVENT + 1
    EVENT_PLAYER_MOVE_DOWN = pygame.USEREVENT + 2
    EVENT_PLAYER_MOVE_LEFT = pygame.USEREVENT + 3
    EVENT_PLAYER_MOVE_UP = pygame.USEREVENT + 4
    EVENT_SPACE = pygame.USEREVENT + 5
    EVENT_TIMER_AT_0 = pygame.USEREVENT + 6
