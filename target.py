import pygame
from random import randint
from pygame.sprite import Sprite

class Target():
    """
    This class controls the opposing pirate ship, such as the settings for the ship like the speed, 
    the direction of travel, the image, and the boundaries.
    """
# Jay    
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
# Resha    
    def blitme(self):
    #the ship is drawn onto the screen and will appear on top of the background
        self.screen.blit(self.image, self.rect)
