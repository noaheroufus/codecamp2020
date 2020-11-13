class Graphic:
    def __init__(self, graphic_list, animation_time_list):
        self.timer = 0
        self.graphics = graphic_list
        self.times = animation_time_list
    def render(self, surface, position):
        surface.blit(self.animate(), position)
    def animate(self):
        # pick which graphic to use based on the timer
        graphic = self.graphics[0]
        # update timer
        self.timer += 1
        if self.timer > self.times[-1]:
            self.timer = 0
        return graphic
