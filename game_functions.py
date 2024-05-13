import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien

def update_bullets(sett, screen, ship, aliens, bullets):
    bullets.update() #poruszanie pociskami

    for bullet in bullets.copy(): #usuwanie pociskow za ekranem
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(sett, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(sett, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        sett.increase_speed()
        create_fleet(sett, screen, ship, aliens)

def check_keydown_events(event, sett, screen, stats, ship, aliens, bullets):
    if event.key == pygame.K_RIGHT: #poruszanie statkiem
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: #poruszanie statkiem
        ship.moving_left = True
    
    elif event.key == pygame.K_q: #wyjscie z gry za pomoca "Q"
        sys.exit()

    elif event.key == pygame.K_SPACE: #ograniczona amunicja
        fire_bullet(sett, screen, ship, bullets)
    
    elif event.key == pygame.K_g:
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(sett, screen, ship, aliens)
        ship.center_ship()

def fire_bullet(sett, screen, ship, bullets): #ograniczona amunicja
    if len(bullets) < sett.bullets_allowed:
        new_bullet = Bullet(sett, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT: #przestanie poruszania statkiem
        ship.moving_right = False
    elif event.key == pygame.K_LEFT: #przestanie poruszania statkiem
        ship.moving_left = False

def check_events(sett, screen, stats, play_button, ship, aliens, bullets):
    for event in pygame.event.get(): #kiedy cos sie zrobi (np kliknie przycisk) petla sie uruchamia
        if event.type == pygame.QUIT: #jezeli kliknie sie X okno sie zamyka
            sys.exit() #zamkniecie okna

        elif event.type == pygame.KEYDOWN: #jezeli przycisk jest klikniety
            check_keydown_events(event, sett, screen, stats, ship, aliens, bullets)
        elif event.type == pygame.KEYUP: #jezeli przycisk jest puszczony
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(sett, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(sett, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(sett, screen, ship, aliens)
        ship.center_ship()

def update_screen(sett, screen, stats, ship, aliens, bullets, play_button):
    screen.fill(sett.bg_color) #kolor tla

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme() #wyswietla statek
    aliens.draw(screen) #wyswietla obcych

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip() #wyswietlanie ostatniego ekranu

def get_number_aliens_x(sett, alien_width):
    available_space_x = sett.screen_width - sett.ilosc_obcych * alien_width
    number_aliens_x = int(available_space_x / (sett.ilosc_obcych * alien_width))
    return number_aliens_x

def get_number_rows(sett, ship_height, alien_height):
    available_space_y = (sett.screen_height - (sett.wysokosc_spawn_obcych * alien_height) - ship_height)
    number_rows = int(available_space_y / (sett.odstep_miedzy_obcymi_pion * alien_height))
    return number_rows

def create_alien(sett, screen, aliens, alien_number, row_number):
    alien = Alien(sett, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + sett.odstep_miedzy_obcymi_poziom * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + sett.odstep_miedzy_obcymi_pion * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(sett, screen, ship, aliens):
    alien = Alien(sett, screen)
    number_aliens_x = get_number_aliens_x(sett, alien.rect.width)
    number_rows = get_number_rows(sett, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(sett, screen, aliens, alien_number, row_number)

def check_fleet_edges(sett, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_direction(sett, aliens)
            break

def change_direction(sett, aliens):
    for alien in aliens.sprites():
        alien.rect.y += sett.drop_speed
    sett.direction *= -1

def ship_hit(sett, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        aliens.empty()
        bullets.empty()

        create_fleet(sett, screen, ship, aliens)
        ship.center_ship()

        sleep(2)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(sett, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(sett, stats, screen, ship, aliens, bullets)
            break

def update_aliens(sett, stats, screen, ship, aliens, bullets):
    check_fleet_edges(sett, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(sett, stats, screen, ship, aliens, bullets)
        print("Statek zostal trafiony!!!")

    check_aliens_bottom(sett, stats, screen, ship, aliens, bullets)