from enemy import Enemy
import random

class RadioWave(Enemy):
    def __init__(self, game, size, graphic):
        #super().__init__(game, (random.randrange(0, game.screen_width), -size[1]), size, graphic)
        super().__init__(game, (game.screen_width/2, size[1]), size, graphic)
        vel = (random.randrange(0, game.screen_width)/20, game.screen_height/20)
        self.set_velocity(vel[0], vel[1])
        #self.set_velocity(random.randrange(0, game.screen_width)/20, game.screen_height/20)

    def update(self):
        super().update()
        #if self.position[1] > self.game.screen_height+self.game.sprite_height:
            #print("deleted self radiowave")
            #self.game.game_objects[self.game.state.get_state()].remove(self)

    def render(self):
        if self.graphic:
            self.graphic.render(self.game.canvas.surface, self.position)
