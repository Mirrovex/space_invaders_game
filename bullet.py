import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, sett, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, sett.bullet_width, sett.bullet_height) #hitbox pocisku
        self.rect.centerx = ship.rect.centerx #wystrzelenie tam gdzie jest statek
        self.rect.top = ship.rect.top #wystrzelenie tam gdzie jest statek

        self.y = float(self.rect.y)

        self.color = sett.bullet_color
        self.speed = sett.bullet_speed
    
    def update(self):
        self.y -= self.speed #poruszanie sie pocisku
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)