import sys
import pygame
from argparse import ArgumentParser

from settings import Settings
from ship import Ship 
from cannonball import CannonBall
from target import Target

class Main:
	"""This is the main class of the game. It is responsbile for running the game and contains/imports 
    		from settings, ship, cannonball and target.
    			 Attributes:
				difficululty (int) sets the level of difficulty for this game via an int value and based on that
				increases the speed of the target making it difficult to hit.
       			"""

	def __init__(self, difficulty):	
		"""This method creates an instane of the game and intializing the difficulty setting of the game. 
    		The code that initializes the pygame library with the settings attribute comes from searching how to use 
     		Pygame's website/tutorials. In addition, when we searched for what we specificall wanted to produce, we found help from help from this site: https://www.codegrepper.com/code-examples/python/set+up+pygame+screen
      		In addition, we found another game that uses the same code for their project so we wanted to cite this:
      		https://github.com/ehmatthes/pcc_2e/blob/master/chapter_13/ending_the_game/alien_invasion.py
       		The modifcations are our own values of the game, such as the caption, and the self.bg_color values. -Arfa """
		
  		pygame.init()
		self.settings = Settings(difficulty)

		# This code initializes the pygame library with the settings attribute of the screen
 		#from the Settings class. This code is used to set the screen's parameters height, width, etc 
		# the syntax was found using pygame codegrepper and we also saw another game referenced in the
		# docstring which used this.
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width 
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Battle")
		self.bg_color = (220, 220, 230)
    
		# initializes the ship and cannonballs (sprite object)
		self.ship = Ship(self)
		self.cannonballs = pygame.sprite.Group()
		self.target = Target(self)

	def _run_(self):
		""" determines based on events when we want to quit the game, and exit out of the game window, this code runs
  
  			side effects: pygame.quit shuts down pygame and sys.exit() shuts down the program
     		
       		source: the tutorial on how to do this was found here: https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self.keydown_events(event)
			elif event.type == pygame.KEYUP:
				self.keyup_events(event)

	def keydown_events(self, event):
    	 """responds to an event (key being pressed) 
      
      		Args:
        		event (int) a key being pressed
        	
         	Side effects:
          		changes the position of the ship 
            
        		Reference: the logic of this is something we came up with but for syntax help, we found a tutorial on this website:
          			https://riptutorial.com/pygame/example/18046/event-loop"""
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.move_left = True 
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self.fire_cannonball()
		       
	def keyup_events(self, event):
		""" responds to an event (key being pressed) in this case, key up event
  	
   			Args:
      			event (int) represented by the keys being pressed 
         
         	Side effects: changes the position of the ship
          	Reference: we found the syntax for this on this website https://riptutorial.com/pygame/example/18046/event-loop 
           				but the logic and the use of using which buttons and moving the ship a certain way was ours"""
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.move_left = False

#Lauren:		
	def start_game(self):
		"""Starts the main while loop of the game
  
		Side effects:
			calls methods of the Main class
  
		"""
		while True:
			self._run_()
			self.ship.update()
			self.target.update()
			self.update_cannonballs()
			self.update_screen()
 
	def update_cannonballs(self):
		"""updates the cannonball's position and deletes the cannonball from the 
  		cannonball list if it exits the screen
		
  		Side effects:
			Prints a message to the console if you successfully hit the target
			and removes a cannonball from the cannonballs attribute everytime
			you miss. 
   
		"""
		self.cannonballs.update()
		for cannonball in self.cannonballs.copy():
				if cannonball.rect.bottom <= 0:
					self.cannonballs.remove(CannonBall)
				
				elif cannonball.rect.bottom == self.target.rect.bottom and cannonball.rect.left > self.target.rect.left and cannonball.rect.right < self.target.rect.right:
					self.cannonballs.remove(CannonBall)
					print("You have hit the target you win!")
					sys.exit()
     		
	def fire_cannonball(self):
		"""initializes a new cannonball on the screen.
	
		Side effects:
			Prints a message if you run out of cannonballs without hitting
			the target. 
  
		"""	
		if len(self.cannonballs) < self.settings.cannonballs_allowed:
			new_cannonball = CannonBall(self)
			self.cannonballs.add(new_cannonball)
		else:
			print("You lose! You ran out of cannonballs")
			sys.exit()
		
	def update_screen(self):
		"""Redraws the screen with every pass through the loop
  
		"""
		self.screen.fill(self.settings.bg_color)
		self.target.blitme()
		self.ship.blitme()
		for cannonball in self.cannonballs.sprites():
			cannonball.draw_cannonball()

		pygame.display.flip()
  
def parse_args(arglist):
	"""Takes a difficulty from the user and sets the ship and target speed
		accordingly. (Parse command-line arguments)

	Args:
		arglist (list of str): arguments from the command line

	Returns:
		namespace: the parsed arguments
  
	"""
	parser = ArgumentParser()
	parser.add_argument("game_difficulty", help="Enter game difficulty (1, 2, 3, 4, 5)")
	return parser.parse_args(arglist)
  
def main(difficulty = 1):
	"""Creates an instance of the Main class

	Args:
		difficulty (int, optional): an integer from 1 to 5 setting the difficulty
  		of the game, defaults to 1.
	"""
	game = Main(difficulty)
	game.start_game()
    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(int(args.game_difficulty))