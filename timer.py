import pygame
from event import Event

class Timer:
    def __init__(self, speed=1, max=32):
        self.timer = 0
        self.subtimer = 0
        self.speed = speed
        self.max = max
    def get_timer(self):
        return self.timer
    def ready(self):
        return (self.timer >= self.max-1 and self.subtimer >= self.speed/2) or (self.timer == 0 and self.subtimer <= self.speed/2)
    def tick(self):
        self.subtimer += 1
        if self.subtimer >= self.speed:
            self.timer += 1
            self.subtimer = 0
        if self.subtimer == 0 and self.timer >= self.max:
            self.timer = 0
            pygame.event.post(pygame.event.Event(Event.EVENT_TIMER_AT_0, {}))
