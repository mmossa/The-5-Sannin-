def __init__(self,ab_game):

    """intializes the plane and sets its positions"""

    self.screen = ab_game.screen
    self.screen_rect = ab_game.screen.get.screen_rect()

    #load image

    self.image = pygame.image.load(""filename")
    self.rect = self.image.get.rect()
    
    ### start plane from below "runway" the screen
    
    self.rect.midbottm = self.screen.rect.midbottom
   
