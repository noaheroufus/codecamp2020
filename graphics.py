import os, pygame

class Graphics:
    def __init__(self):
        self.load_images()
    def load_images(self):
        self.player_idle = pygame.image.load(os.path.join('graphics', 'player_idle.png')).convert_alpha()
        self.player_walk_0 = pygame.image.load(os.path.join('graphics', 'player_walk_0.png')).convert_alpha()
        self.player_walk_1 = pygame.image.load(os.path.join('graphics', 'player_walk_1.png')).convert_alpha()
        self.player_walk_2 = pygame.image.load(os.path.join('graphics', 'player_walk_2.png')).convert_alpha()
        self.player_hang = pygame.image.load(os.path.join('graphics', 'player_hang.png')).convert_alpha()
        self.player_hang_jump = pygame.image.load(os.path.join('graphics', 'player_hang_jump.png')).convert_alpha()
        self.player_hang_jump_left = pygame.image.load(os.path.join('graphics', 'player_hang_jump_left.png')).convert_alpha()
        self.player_hang_jump_right = pygame.image.load(os.path.join('graphics', 'player_hang_jump_right.png')).convert_alpha()
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
        self.rung = pygame.image.load(os.path.join('graphics', 'rung.png')).convert_alpha()
        self.rung_frozen = pygame.image.load(os.path.join('graphics', 'rung_frozen.png')).convert_alpha()
        self.rung_packet = pygame.image.load(os.path.join('graphics', 'rung_packet.png')).convert_alpha()
        self.rung_upgrade_station = pygame.image.load(os.path.join('graphics', 'rung_upgrade_station.png')).convert_alpha()
        self.wrench = pygame.image.load(os.path.join('graphics', 'wrench.png')).convert_alpha()
        self.battery = pygame.image.load(os.path.join('graphics', 'battery.png')).convert_alpha()
        self.jammer = pygame.image.load(os.path.join('graphics', 'jammer.png')).convert_alpha()
        self.dish = pygame.image.load(os.path.join('graphics', 'dish.png')).convert_alpha()
        self.menu = pygame.image.load(os.path.join('graphics', 'menu.png')).convert_alpha()
        self.game_over = pygame.image.load(os.path.join('graphics', 'game_over.png')).convert_alpha()
        self.menu_c = pygame.image.load(os.path.join('graphics', 'menu_c.png')).convert_alpha()
        self.menu_n = pygame.image.load(os.path.join('graphics', 'menu_n.png')).convert_alpha()
        self.menu_ne = pygame.image.load(os.path.join('graphics', 'menu_ne.png')).convert_alpha()
        self.menu_e = pygame.image.load(os.path.join('graphics', 'menu_e.png')).convert_alpha()
        self.menu_se = pygame.image.load(os.path.join('graphics', 'menu_se.png')).convert_alpha()
        self.menu_s = pygame.image.load(os.path.join('graphics', 'menu_s.png')).convert_alpha()
        self.menu_sw = pygame.image.load(os.path.join('graphics', 'menu_sw.png')).convert_alpha()
        self.menu_w = pygame.image.load(os.path.join('graphics', 'menu_w.png')).convert_alpha()
        self.menu_nw = pygame.image.load(os.path.join('graphics', 'menu_nw.png')).convert_alpha()
        self.heart_full = pygame.image.load(os.path.join('graphics', 'heart_full.png')).convert_alpha()
        self.heart_half = pygame.image.load(os.path.join('graphics', 'heart_half.png')).convert_alpha()
        self.menu_arrow = pygame.image.load(os.path.join('graphics', 'menu_arrow.png')).convert_alpha()
        self.enemy_bug_1 = pygame.image.load(os.path.join('graphics', 'bug_1.png')).convert_alpha()
        self.armour = pygame.image.load(os.path.join('graphics', 'armour_indicator.png')).convert_alpha()
        self.background_blank = pygame.image.load(os.path.join('graphics', 'background_blank.png')).convert_alpha()