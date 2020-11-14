class TurnCounter():
    TURN_PLAYER = 0
    TURN_ENEMY = 1

    def __init__(self, turn_list=[self.TURN_PLAYER, self.TURN_ENEMY]):
        self.turn_list = turn_list
        self.turn_index = 0
        self.turn_number = 0;

    def turn_advance(self):
        self.turn_index += 1
        if self.turn_index >= len(self.turn_list):
            self.turn_index = 0
            self.turn_number += 1
