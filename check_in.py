from random import randint

class Battleship:
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
