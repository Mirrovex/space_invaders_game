import pygame

class Ship():
    def __init__(self, sett, screen):
        self.screen = screen
        self.sett = sett
        self.image = pygame.image.load("obrazki\\statek 2.png") #wczytanie obrazu
        self.rect = self.image.get_rect() #powierzchnia obiektu (hitbox)
        self.screen_rect = screen.get_rect() #powierzchnia okna

        self.rect.centerx = self.screen_rect.centerx #wysrodkowanie statku
        self.rect.bottom = self.screen_rect.bottom #ustawianie statku na dole

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: #poruszanie statkiem i zeby statek nie wyszedl za okno
            self.center += self.sett.ship_speed
        if self.moving_left and self.rect.left > 0: #poruszanie statkiem i zeby statek nie wyszedl za okno
            self.center -= self.sett.ship_speed

        self.rect.centerx = self.center #srodek statku jest na srodku ekranu

    def blitme(self): #wyswietlanie obiektu
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        self.center = self.screen_rect.centerx