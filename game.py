import sys,pygame
from graphics import Graphics
from graphic import Graphic
from object import Object
from canvas import Canvas
from player import Player
from event import Event
from state import State
from timer import Timer
from action_timer import ActionTimer
from ladder import Ladder
import random
from random import randint

class Game:
    sprite_size = sprite_width, sprite_height = 32, 32
    screen_size = screen_width, screen_height = 320, 224
    screen_scale = 2
    screen = False
    canvas = False
    running = False
    state = State()
    clock = False
    tps = 60
    game_objects = [[],[],[],[]]
    clouds = []

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width*self.screen_scale, self.screen_height*self.screen_scale))
        pygame.display.set_caption("InfoWest Tower Security")
        self.clock = pygame.time.Clock()
        self.graphics = Graphics()
        self.canvas = Canvas(self)

        self.timer = Timer()

        # === Game Objects ===
        self.title_screen = Object(self, (0,0), self.screen_size, Graphic([self.graphics.title_screen], [0]))
        self.background = Object(self, (0,0), self.screen_size, Graphic([self.graphics.background], [0]))
        self.player = Player(self, (((self.screen_width/self.sprite_width)/2)*self.sprite_width, self.screen_height-self.sprite_height), (32,32), Graphic([self.graphics.player_walk_0, self.graphics.player_walk_1, self.graphics.player_walk_2],[10, 10, 10]))
        self.ladder = Ladder(self, int(self.screen_width/self.sprite_width), int(self.screen_height/self.sprite_height), (0,0))
        self.game_over = Object(self, (0,0), self.screen_size, Graphic([self.graphics.game_over], [0]))
        self.game_objects[State.STATE_GAME_MENU].append(self.title_screen)
        self.game_objects[State.STATE_GAME_CLIMB].append(self.background)
        for i in range(7):
            cloudtype = randint(0,2)
            types = [self.graphics.cloud_1, self.graphics.cloud_2, self.graphics.cloud_3]
            cloud = Object(self, (randint(0, self.screen_width),randint(0, 170)), (24,24), Graphic([types[cloudtype]], [0]))
            self.clouds.append(cloud)
            cloud.set_velocity(random.uniform(1, 1.5), 0)
            self.game_objects[State.STATE_GAME_CLIMB].append(cloud)
        self.game_objects[State.STATE_GAME_CLIMB].append(self.player)
        self.game_objects[State.STATE_GAME_BATTLE].append(self.background)
        self.game_objects[State.STATE_GAME_BATTLE].append(self.player)
        self.game_objects[State.STATE_GAME_OVER].append(self.game_over)
        self.game_objects[State.STATE_GAME_CLIMB].append(self.ladder)

        timer_lengths = []
        for i in range(self.timer.max):
            timer_lengths.append(self.timer.max/8)
        self.action_timer = ActionTimer(self, (0,0), self.sprite_size, Graphic([self.graphics.timer_face], [0]), Graphic([self.graphics.timer_needle_n, self.graphics.timer_needle_ne, self.graphics.timer_needle_e, self.graphics.timer_needle_se, self.graphics.timer_needle_s, self.graphics.timer_needle_sw, self.graphics.timer_needle_w, self.graphics.timer_needle_nw], timer_lengths))
        self.game_objects[State.STATE_GAME_CLIMB].append(self.action_timer)

        self.ladder = Ladder(self, int(self.screen_width/self.sprite_width), int(self.screen_height/self.sprite_height), (0,0))
        self.game_objects[State.STATE_GAME_CLIMB].append(self.ladder)
        self.game_objects[State.STATE_GAME_CLIMB].append(self.player)
        self.game_objects[State.STATE_GAME_BATTLE].append(self.player)

    def update(self):
        self.clock.tick(self.tps)
        self.timer.tick()

        self.handle_inputs()
        self.handle_events()
        
        if self.player.get_health() == 0:
            self.state.set_state(State.STATE_GAME_OVER)
        for obj in self.game_objects[self.state.get_state()]:
            obj.update()

        for cloud in self.clouds:
            if cloud.position[0] > self.screen_width:
                cloud.position = (-16, randint(0, self.screen_height))

    
    def render(self):
        self.canvas.render()
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
            pygame.event.post(pygame.event.Event(Event.EVENT_KEY_PRESSED, key=pygame.K_RIGHT))
        if keys[pygame.K_DOWN]:
            pygame.event.post(pygame.event.Event(Event.EVENT_KEY_PRESSED, key=pygame.K_DOWN))
        if keys[pygame.K_LEFT]:
            pygame.event.post(pygame.event.Event(Event.EVENT_KEY_PRESSED, key=pygame.K_LEFT))
        if keys[pygame.K_UP]:
            pygame.event.post(pygame.event.Event(Event.EVENT_KEY_PRESSED, key=pygame.K_UP))
        if keys[pygame.K_SPACE]:
            pygame.event.post(pygame.event.Event(Event.EVENT_KEY_PRESSED, key=pygame.K_SPACE))
        if keys[pygame.K_q]:
            pygame.event.post(pygame.event.Event(Event.EVENT_KEY_PRESSED, key=pygame.K_q))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == Event.EVENT_KEY_PRESSED:
                if event.key == pygame.K_SPACE:
                    if self.state.get_state() != State.STATE_GAME_CLIMB:
                        self.state.set_state(State.STATE_GAME_CLIMB)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.event.post(pygame.event.Event(Event.EVENT_CHANGE_ITEM, {}))
                if event.key == pygame.K_SPACE:
                    if self.state.get_state() != State.STATE_GAME_MENU and self.state.get_state() != State.STATE_GAME_OVER:
                        pygame.event.post(pygame.event.Event(Event.EVENT_USE_ITEM, {}))
            self.player.handle_event(event)
