import pygame

class Ship: 
    #Mossa
    """
    This is the class in which the ship object is being manged. 
    https://github.com/ehmatthes/pcc_2e/blob/master/chapter_13/ending_the_game/ship.py
    Attributes:
          game: the game's current instance
    """
    def __init__(self, game): 
        """
        Set the object's image and initial image location after initializing it.
        """
        self.screen = game.screen
        self.settings = game.settings
        
        # load image and set the position to midbottom
        self.image = pygame.image.load("./boat.png")
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        
        # is ship is moving right or left, or up or down
        self.move_right = False
        self.move_left = False
        
    def update(self):
        """
        This function updates ship position based on if move_right or move_left is True
        """
        if self.move_right and self.rect.right <= self.screen_rect.right:
            # check if the rect right is less than the screen_rect's right (right edge of screen)
            self.rect.x += self.settings.move_speed
            # update rect x position by the amount to move
        
        if self.move_left and self.rect.left >= 0:
            # check if the rect left is greater than 0 (left edge of screen)
            self.rect.x -= self.settings.move_speed
            # update rect x position by the amount to move
            
        
    def blitme(self):
        """
        This method raws the ship from its current position
        """
        self.screen.blit(self.image, self.rect) 
