""" Simulate a game where the user shoots cannonballs at the moving ship. """

import pygame
from pygame.sprite import Sprite 

class CannonBall(Sprite):
    """Manages the cannonballs shot at the ship object.
    
    Attributes: 
		game: the current instance for the game.
    """
    def __init__(self, game):
    	""" 
        We use the super() function to make inheritance more manageable from Sprite.
        """
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings

		# create the rect for the cannonball
		self.color = self.settings.cannonball_color	
		self.rect = pygame.Rect(0,0, self.settings.cannonball_width, self.settings.cannonball_height)
		self.rect.midtop = game.ship.rect.midtop
 	
	def update(self):
		# update cannonball rect y postion by cannonball speed
		self.rect.y -= self.settings.cannonball_speed

	def draw_cannonball(self):
		# draw the cannonball rect onto the screen
	    pygame.draw.rect(self.screen, self.color, self.rect)
