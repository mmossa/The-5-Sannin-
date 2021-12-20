import pygame
from random import randint
from pygame.sprite import Sprite

class Target():
    
    def __init__ (self, game):
        self.screen = game.screen
        self.settings = game.settings
        
        # initialize target image and position
        self.image = pygame.image.load("./target.png")
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.rect.midtop = self.screen_rect.midtop
        
        self.direction = 1;
# Arfa      
    def update(self):
        """move the target in positive or negative direction and swithces position based on right/left side
                
            Side effects: if target reaches the left side of the screen, switches direction to positive
                         if reaches the right side of the screen, switch direction to negative
"""
        
        self.rect.x += randint(self.settings.target_min_speed, self.settings.target_max_speed) * self.direction
    
        if self.rect.left <= 0: 
            self.direction = 1
        elif self.rect.right >= self.screen_rect.right:
            self.direction = -1
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)