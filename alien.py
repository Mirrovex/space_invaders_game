import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, sett, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.sett = sett

        self.image = pygame.image.load('obrazki\\obcy 1.jpg')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.sett.alien_speed * self.sett.direction)
        self.rect.x = self.x