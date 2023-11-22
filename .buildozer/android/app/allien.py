import pygame
from pygame.sprite import Sprite
import random

class Allien(Sprite):
    def __init__(self, ai_settings, screen) -> None:
        super(Allien,self).__init__()
        self.ai_setting=ai_settings
        self.screen=screen

        #load image 
        self.image = [pygame.image.load("images/rb.bmp"),pygame.image.load("images/allien2.bmp")]
        self.image=random.choice(self.image)
        self.rect =self.image.get_rect()

        #start at the top left corner
        self.rect.x= self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def check_edge(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
    def update(self):
        """move the allien to the right"""
        self.x+=(self.ai_setting.allien_speed_factor* self.ai_setting.fleet_direction)
        self.rect.x=self.x
    