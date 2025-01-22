class Place():

    # Calculate % changes in area based on the following variables:
    WIND_SPEED = None
    ELEVATION = None
    WIND_CHANGE = None
    MOISTURE_LEVELS = None
    PERCENT_CHANCE_OF_FIRE = None

    latitude = None
    longitude = None

    def __init__(self, x, y):
        self.latitude = x
        self.longitude = y

    
    def get_x(self):
        return self.latitude
    
    
    def get_y(self):
        return self.longitude
    
    

