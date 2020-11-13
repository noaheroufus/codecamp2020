class State:
    STATE_GAME_MENU = 0
    STATE_GAME_OVER = 1
    STATE_GAME_BATTLE = 2
    STATE_GAME_CLIMB = 3

    state = 0

    def __init__(self):
        self.state = self.STATE_GAME_MENU

    def get_state(self):
        return self.state
    
    def set_state(self, state):
        self.state = state
