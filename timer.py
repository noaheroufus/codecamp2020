class Timer:
    def __init__(self, speed=1, max=10):
        self.timer = 0
        self.subtimer = 0
        self.speed = speed
        self.max = max
    def get_timer(self):
        return self.timer
    def tick(self):
        self.subtimer += 1
        if self.subtimer >= self.speed:
            self.timer += 1
            self.subtimer = 0
        if self.timer >= self.max:
            self.timer = 0
