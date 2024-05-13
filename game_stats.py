class GameStats():
    def __init__(self, sett):
        self.sett = sett
        self.reset_stats()

        self.game_active = False
        
    def reset_stats(self):
        self.ships_left = self.sett.ship_limit