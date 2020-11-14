from object import Object
import random
from graphic import Graphic

class Enemy(Object):
    def __init__(self, game, position, size, armour=100, health=100, graphic=False):
        super().__init__(game, position, size, graphic)
        self.armour = armour
        self.health = health
        self.weapon = 5
        self.alive = True
        self.choices = [self.attack, self.defend]
        self.weights = [0.9, 0.1]
        self.defending = False
        self.armour_image = Graphic([self.game.graphics.enemy_armour], [0])

    def get_armour(self):
        if self.defending: armour = self.armour + 20
        else: armour = self.armour
        return armour

    def act(self):
        random.choices(self.choices, self.weights, k=1)[0](self.game.player)
        self.game.turn_counter.turn_advance()

    def attack(self, player):
        # hurt player
        player.damage(self.weapon)

    def defend(self, player):
        # increase armour
        self.defending = True

    def damage(self, weight):
        print("Enemy damaged")
        if self.armour > 0:
            new_armour = self.get_armour() - weight
            if self.armour > new_armour: self.armour = new_armour
        else:
            self.health -= weight
            if self.health <= 0: self.alive = False

    def render(self):
        super().render()
        if self.armour > 0:
            self.armour_image.render(self.game.canvas.surface, self.position)
