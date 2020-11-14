import os, pygame

class Graphics:
    def __init__(self):
        self.load_images()
    def load_images(self):
        self.player_idle = pygame.image.load(os.path.join('graphics', 'player_idle.png')).convert_alpha()
        self.player_walk_0 = pygame.image.load(os.path.join('graphics', 'player_walk_0.png')).convert_alpha()
        self.player_walk_1 = pygame.image.load(os.path.join('graphics', 'player_walk_1.png')).convert_alpha()
        self.player_walk_2 = pygame.image.load(os.path.join('graphics', 'player_walk_2.png')).convert_alpha()
        self.background = pygame.image.load(os.path.join('graphics', 'background.png')).convert_alpha()
        self.cloud_1 = pygame.image.load(os.path.join('graphics', 'cloud_1.png')).convert_alpha()
        self.cloud_2 = pygame.image.load(os.path.join('graphics', 'cloud_2.png')).convert_alpha()
        self.cloud_3 = pygame.image.load(os.path.join('graphics', 'cloud_3.png')).convert_alpha()
        self.timer_face = pygame.image.load(os.path.join('graphics', 'timer_face.png')).convert_alpha()
        self.timer_needle_n = pygame.image.load(os.path.join('graphics', 'timer_needle_n.png')).convert_alpha()
        self.timer_needle_ne = pygame.image.load(os.path.join('graphics', 'timer_needle_ne.png')).convert_alpha()
        self.timer_needle_e = pygame.image.load(os.path.join('graphics', 'timer_needle_e.png')).convert_alpha()
        self.timer_needle_se = pygame.image.load(os.path.join('graphics', 'timer_needle_se.png')).convert_alpha()
        self.timer_needle_s = pygame.image.load(os.path.join('graphics', 'timer_needle_s.png')).convert_alpha()
        self.timer_needle_sw = pygame.image.load(os.path.join('graphics', 'timer_needle_sw.png')).convert_alpha()
        self.timer_needle_w = pygame.image.load(os.path.join('graphics', 'timer_needle_w.png')).convert_alpha()
        self.timer_needle_nw = pygame.image.load(os.path.join('graphics', 'timer_needle_nw.png')).convert_alpha()
        self.title_screen = pygame.image.load(os.path.join('graphics', 'title_screen.png')).convert_alpha()

