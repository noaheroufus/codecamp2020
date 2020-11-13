import sys,pygame
from graphics import Graphics
from graphic import Graphic
from object import Object
from canvas import Canvas
from player import Player
from event import Event

class Game:
    screen_size = screen_width, screen_height = 320, 240
    screen_scale = 2
    screen = False
    canvas = False
    running = False
    clock = False
    tps = 60
    objects = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width*self.screen_scale, self.screen_height*self.screen_scale))
        pygame.display.set_caption("InfoWest Tower Security")
        self.clock = pygame.time.Clock()
        self.graphics = Graphics()
        self.canvas = Canvas(self)

        self.player = Player(self, (self.screen_width/2, self.screen_height/2), (32,32), Graphic([self.graphics.player_walk_0, self.graphics.player_walk_1, self.graphics.player_walk_2],[10, 10, 10]))

        self.objects.append(self.player)

    def update(self):
        self.clock.tick(self.tps)

        self.handle_inputs()
        self.handle_events()
        
        for obj in self.objects:
            obj.update()
    
    def render(self):
        self.canvas.render(self.objects)
        pygame.display.flip()

    def loop(self):
        self.running = True
        while self.running:
            self.update()
            self.render()
        
        sys.exit()

    def handle_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.event.post(pygame.event.Event(pygame.QUIT, {}))
        if keys[pygame.K_RIGHT]:
            pygame.event.post(pygame.event.Event(Event.EVENT_PLAYER_MOVE_RIGHT, {}))
        if keys[pygame.K_DOWN]:
            pygame.event.post(pygame.event.Event(Event.EVENT_PLAYER_MOVE_DOWN, {}))
        if keys[pygame.K_LEFT]:
            pygame.event.post(pygame.event.Event(Event.EVENT_PLAYER_MOVE_LEFT, {}))
        if keys[pygame.K_UP]:
            pygame.event.post(pygame.event.Event(Event.EVENT_PLAYER_MOVE_UP, {}))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            self.player.handle_event(event)
