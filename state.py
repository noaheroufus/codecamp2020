class State:
    STATE_GAME_MENU = 1
    STATE_GAME_PLAY = 2
    STATE_GAME_OVER = 3

    state = 0

    def __init__(self):
        self.state = self.STATE_GAME_MENU

    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state