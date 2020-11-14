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
from menu import Menu
from text import Text

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
        self.game_objects[State.STATE_GAME_MENU].append(self.title_screen)
        self.game_objects[State.STATE_GAME_CLIMB].append(self.background)
        self.game_objects[State.STATE_GAME_BATTLE].append(self.background)
        self.game_objects[State.STATE_GAME_CLIMB].append(self.ladder)

        timer_lengths = []
        for i in range(self.timer.max):
            timer_lengths.append(self.timer.max/8)
        self.action_timer = ActionTimer(self, (0,0), self.sprite_size, Graphic([self.graphics.timer_face], [0]), Graphic([self.graphics.timer_needle_n, self.graphics.timer_needle_ne, self.graphics.timer_needle_e, self.graphics.timer_needle_se, self.graphics.timer_needle_s, self.graphics.timer_needle_sw, self.graphics.timer_needle_w, self.graphics.timer_needle_nw], timer_lengths))
        self.game_objects[State.STATE_GAME_CLIMB].append(self.action_timer)

        self.menu_battle = Menu(self, (0, self.screen_height), ["Attack", "Defend", "Item", "FLEE", "FLEE", "FLEE", "FLEE", "FLEE", "FLEE", "FLEE"], pointer=Graphic([self.graphics.battery], [0]))
        self.game_objects[State.STATE_GAME_BATTLE].append(self.menu_battle)
        self.game_objects[State.STATE_GAME_CLIMB].append(self.player)
        self.game_objects[State.STATE_GAME_BATTLE].append(self.player)

    def update(self):
        self.clock.tick(self.tps)
        self.timer.tick()

        self.handle_inputs()
        self.handle_events()

        for obj in self.game_objects[self.state.get_state()]:
            obj.update()

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

    def new_state(self, state):
        self.state.set_state(state)
        if state == State.STATE_GAME_BATTLE:
            self.player.velocity=[0,0]
            self.player.graphic.graphics = [self.graphics.player_idle]
            self.player.graphic.times = [1]
            self.player.position = (((self.screen_width/self.sprite_width)/2)*self.sprite_width, self.screen_height-self.sprite_height)
        if state == State.STATE_GAME_CLIMB:
            self.ladder.__init__(self, int(self.screen_width/self.sprite_width), int(self.screen_height/self.sprite_height), (0,0))
            self.player.set_health(100)
            self.player.previous_rung = (0,0)
            self.player.velocity = (0,0)
            self.player.position = (((self.screen_width/self.sprite_width)/2)*self.sprite_width, self.screen_height-self.sprite_height)


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.event.post(pygame.event.Event(Event.EVENT_CHANGE_ITEM, {}))
                if event.key == pygame.K_SPACE:
                    if self.state.get_state() == State.STATE_GAME_MENU:
                        pygame.event.post(pygame.event.Event(Event.EVENT_CHANGE_STATE, state=State.STATE_GAME_CLIMB))
                    if self.state.get_state() == State.STATE_GAME_OVER:
                        pygame.event.post(pygame.event.Event(Event.EVENT_CHANGE_STATE, state=State.STATE_GAME_CLIMB))
                    elif self.state.get_state() != State.STATE_GAME_MENU and self.state.get_state() != State.STATE_GAME_OVER:
                        pygame.event.post(pygame.event.Event(Event.EVENT_USE_ITEM, {}))
                if self.state.get_state() == State.STATE_GAME_BATTLE:
                    self.menu_battle.handle_event(event)
            if event.type == Event.EVENT_CHANGE_STATE:
                self.canvas.transition(event.state)
            self.player.handle_event(event)
