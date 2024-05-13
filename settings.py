class Settings():
    def __init__(self):
        #ekran
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        #statek
        self.ship_speed = 1.5
        self.ship_limit = 3 #zycia

        #pocisk
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3 #amunicja

        #obcy
        self.odstep_miedzy_obcymi_poziom = 1.5 #obcego
        self.odstep_miedzy_obcymi_pion = 1.5 #obcego
        self.ilosc_obcych = 1.4 #im wieksza wartosc tym mniej obcych
        self.wysokosc_spawn_obcych = 3 #obcego
        self.alien_speed = 0.2
        self.drop_speed = 10 #szybkosc spadania obcych
        self.direction = 1 #strona w ktora zaczynaja poruszac sie obcy (1 = prawo, -1 = lewo)

        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale