from object import Object

class ActionTimer(Object):
    def __init__(self, game, position, size, background, needle):
        super().__init__(game, position, size)
        self.bg = background
        self.needle = needle

    def render(self):
        self.bg.render(self.game.canvas.surface, self.position)
        self.needle.render(self.game.canvas.surface, self.position)
