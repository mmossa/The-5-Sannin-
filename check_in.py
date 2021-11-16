from random import randint

def playing_board(board):
  ### Sajjad
    """
    This Function represents the gaming board that we will be running the game on.
    Args:
        board(list): This is an empty list 
    """
    print('   0 1 2 3 4 5')
    print('  |-----------|')

    for row in range(5):
        board.append(['-'] * 5)

    letter = 0

    for row in range(5):
        print(chr(letter + 65), end = ' | ')
        for column in range(len(board[letter])):
            print(board[letter][column], end=' ')
        print('| ')
        letter += 1
    print('  |-----------|')

    print(board)
class Battleship:
  ### Lauren
  """This class sets the location of a ship that is two spaces in lenght
  Attributes:
    location(list): The location of the two unit ship
    orientation(str): The orientation of the ship (horizontal or vertical)

  """
  def __init__(self):
    """This method determines if the ship is horizontal or vertical and 
    initializes the location attribute as a list

    Side effects:
      sets the orientation attribute based on the randint result and initializes
      the location attribute as a list

    """
    self.location = []
    if randint(1,2) == 2:
      self.orientation = "horizontal"
    else:
      self.orientation = "vertical"
  
  def set_location(self):
    """This method sets the location of the two unit ship
    
    Side effects:
      populates the location attribute with two ship coordinates

    """
    row =  [1, 2, 3, 4, 5]
    column = ["A", "B", "C", "D", "E"]
    if self.orientation == "horizontal":
      ship_row = row[randint(0,4)]
      ship_column = column[randint(0,4)]
      self.location.append(str(ship_row)+ str(ship_column))
      if ship_column == "E":
        pos2 = column.index(ship_column) - 1
      else:
        pos2 = column.index(ship_column) + 1
      self.location.append(str(ship_row) + str(column[pos2]))
     
    if self.orientation == "vertical":
      ship_row = row[randint(0,4)]
      ship_column = column[randint(0,4)]
      self.location.append(str(ship_row) + str(ship_column))
      if ship_row < 5:
        pos2 = row.index(ship_row) + 1 
      else:
        pos2 = row.index(ship_row) - 1
      self.location.append(str(row[pos2]) + str(ship_column))
  
  def __repr__(self):
    """A method to correctly display the position of the ship
    
    Returns:
     The two positions in the self.location list
    """
    return f"{self.location[0]} {self.location[1]}"
  
a = Battleship() 
a.set_location() 
print(a) 

### Bullets.py 
### Arfa and Resha 
### This will be a separate .py file that will fire bullets. Ideally, we want the bullets to be fired when player presses the spacebar and travel up the screen
### until they disappear off the screeen. We are going to use pygame module that has objects which we will use to emulate tbe bullets. Module is called "Sprite"

Class Bullets(Sprite):  
  """ A class to manage bullets fired from the plane/ship"""
  import pygame
  from pygame.sprite import Sprite 
 
  def __innit__(self, ab)
   """Create a bullet object at the plane's current location
   
     Attribute:
        ab: this comes from the main file, ab is an instance of the game and runs the game 
          """
    
   
    super().__init__()
    self.screen = ab_game.screen
    self.settings = ab_game.settings
    self.color = self.settings.bullet_color
    
    ### create a bullet rectange area at a coordinate (0,0) and then sets accruate position 
    
    self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
    self.rect.midtop = ab_game.plane.rect.midtop
    
    ### store the bullet's position as a decimal value 
    self.y = float(self.rect.y)
    
  ### Resha's code
  
 def update(self):
  """This method will show how to move bullets up the screen"""
  
   ###Updates position (decimal value) of the bullet  
   self.y -= self.settings.bullet_speed ###when a bullet is fired, it moves up the screen and decreases the y value. In order to update the postion,
   ###we subtract the amount stored in settings.bullet_speed from self.y
    
   ### update rect position
   self.rect.y = self.y
        
 def draw_bullets(self):
   """This method draws the bullets to the screen"""
   pygame.draw.rect(self.screen, self.color, self.rect)

