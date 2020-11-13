class Graphic:
    def __init__(self, graphic_list, animation_time_list):
        self.timer = 0
        self.position = 0
        self.graphics = graphic_list
        self.times = animation_time_list
    def render(self, surface, position):
        surface.blit(self.animate(), position)
    def animate(self):
        # Pick which graphic to use based on the timer
        if self.timer >= self.times[self.position]:  # Advance positions
            self.position += 1
            self.timer = 0
            # Reset position when past the end
            if self.position >= len(self.graphics):
                self.position = 0
        graphic = self.graphics[self.position]
        # update timer
        self.timer += 1
        return graphic
