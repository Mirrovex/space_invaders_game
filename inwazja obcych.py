import pygame
from pygame.sprite import Group

from settings import Settings #import pliku z ustawieniami
from game_stats import GameStats
from button import Button
from ship import Ship #import pliku ze statkiem
from alien import Alien
import game_functions as gf #import pliku z funkcjami gry

def run_game():
    pygame.init() #wywolanie okna
    sett=Settings()
    screen = pygame.display.set_mode((sett.screen_width, sett.screen_height)) #rozmiar okna
    pygame.display.set_caption("Inwazja obcych") #nazwa okna

    play_button = Button(sett, screen, 'Kliknij "G"')

    stats = GameStats(sett)

    ship=Ship(sett, screen) #statek
    bullets = Group()
    aliens = Group()
    gf.create_fleet(sett, screen, ship, aliens)

    while True: #glowna petla gry
        gf.check_events(sett, screen, stats, play_button, ship, aliens, bullets) #sprawdza czy dzieje sie jakas akcja

        if stats.game_active:
            ship.update() #poruszanie statku
            gf.update_bullets(sett, screen, ship, aliens, bullets) #poruszanie pociskami
            gf.update_aliens(sett, stats, screen, ship, aliens, bullets) #poruszanie obcymi

        gf.update_screen(sett, screen, stats, ship, aliens, bullets, play_button) #odswierzanie ekranu
 
run_game()