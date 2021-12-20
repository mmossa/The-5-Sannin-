# The-5-Sannin-
Final Project 

Description of the Project

This project is called Pirate Ship. It is an interactive game that uses Pygame for its visual and interactive effects. 
The aim of the game is for one pirate ship to aim cannonballs at a target (another ship above it). 
The user wins this game if he/she is able to hit the ship within the limitation placed (on the number of cannonballs the user has avaible to be able to hit the other ship) and being actually able to hit the target. At that point, the game ends.

How does it work?
In order for users to run this game, they would need to have the pygame library installed. Then, users can run the game from the Main.py file. 

Project Files 

# Main.py

 This is the file from which our program is run. It's purpose is to start the main loop of the game, and call our other classes that we have created (settings, cannonballs, ship, target). It also initializes the game board, updates the screen, cannonballs, and checks for when the user presses the up, down, left, or right arrow keys. Once the Main.py file is run, it will prompt the user to select a difficulty setting between 1 and 5. This adjusts the speed of the target/ship. If the user successfully hits the target within 5 shots, they win and the terminal will print a winning message. If the user misses all five shots, the terminal will print out a losing message. 

# Cannonball.py

 add description

# Ship.py

 add description 

# Target.py

 add description 

# Settings.py

 add description 

# Bibliography  

Matthes, Eric. “Pcc_2e/alien_invasion.Py at Master · Ehmatthes/pcc_2e.” GitHub, 1 May 2019, https://github.com/ehmatthes/pcc_2e/blob/master/chapter_13/ending_the_game/alien_invasion.py. 

Although we didn't use the code specifically from here, the way we wanted to implement aspects of pygame we saw that this person also uses/writes it in the same syntax/style so we wanted to cite this source because of similiaries we found and if they came up with how to use pygame, we wanted to give them credit for it. Mostly, we saw similiarites in how to set the screen and other object settings in the Main.py file. 

Conrad, P. “Pygame Drawing Basics.” Pygame Drawing Basics, UC Santa Barbara, 2007, https://sites.cs.ucsb.edu/~pconrad/cs5nm/topics/pygame/drawing/. 

  Aside from pygame documentation, this website came up when we were trying to write the code for how to exit/quit out of the game window in the Main.py file.  

Pygame Front Page¶.” Pygame Front Page - Pygame v2.1.1 Documentation, https://www.pygame.org/docs/. 

  We consulted this documentation page to find an easier way to animate our game. For example, from loading the image of our ship (looking at how to import an image, how to move an image, finding out how to redraw the screen (blitme method) to using rect attribute and even finding out what most of these were used for. To creating objects which in our case were cannonballs, (using sprite). Basically, we used the "most useful stuff" to find out how to incorporate various pygame methods/functions in our game. 

“Pygame Tutorial =&gt; Event Loop.” Pygame Tutorial =&gt; Event Loop, Rip Tutorial , https://riptutorial.com/pygame/example/18046/event-loop. 

  This website was used for help with syntax of using pygame event functinality since we wanted to ship to move with pressing certain buttons. 
  
  
Matthes, Eric. “Pcc_2e/alien_invasion.Py at Master · Ehmatthes/pcc_2e.” GitHub, 1 May 2019
https://github.com/ehmatthes/pcc_2e/blob/master/chapter_13/ending_the_game/settings.py 

Even though we did not use the code we saw that this person also uses it in the same syntax/style as we wanted to implement aspects of our settings file, so we wanted to cite this source because of the similarities we discovered. 
