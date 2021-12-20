class Settings:
    
    """
    This class allows us to store all of 
    the game settings that we have set for our ship game. 
    Such as the bullet settings, what speed it travels at, and the color and size of it. 
    """
    def __init__(self, difficulty):
        """
        We initialize the settings here for the cannon ball thats being shot out of the ship. 
        The cannon ball settings, ship settings, target speed settings based on the level of difficulty, and the pygame settings. 
        """
        # cannonball settings
        self.cannonball_speed = 5.0
        self.cannonball_width = 10
        self.cannonball_height = 10 
        self.cannonball_color = (55, 60, 65)
        self.cannonballs_allowed = 5
           
        # ship settings 
        self.move_speed = 15.0
        
        # target speed settings 
        if difficulty <= 1:
            self.target_min_speed = 1.0
            self.target_max_speed = 3.0
        elif difficulty == 2:
            self.target_min_speed = 4.0
            self.target_max_speed = 6.0
        elif difficulty == 3:
            self.target_min_speed = 7.0
            self.target_max_speed = 9.0
        elif difficulty == 4:
            self.target_min_speed = 10.0
            self.target_max_speed = 15.0
        elif difficulty >= 5:
            self.target_min_speed = 15.0
            self.target_max_speed = 25.0
            

        # pygame settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 220, 230)
