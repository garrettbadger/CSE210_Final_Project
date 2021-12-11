from game import constants
import random
from game.actor import Actor
from game.point import Point

class Asteroid(Actor):
    def __init__(self):
        super().__init__()
    
    def create_asteroid():
       
        asteroid = Asteroid()
        asteroid.set_height(constants.ASTEROID_HEIGHT)
        asteroid.set_width(constants.ASTEROID_WIDTH)
        asteroid.set_image(r'asteroids\assets\asteroid(80x80).png')
        x = random.randint(0, 800)
        y = random.randint(10, 15)
        
        
        
       
        position = Point(x, y)
        asteroid.set_position(position)
        # if x <= 50:
            
        #     if y >= 550:
        #         velocity = Point(constants.ASTEROID_DX , constants.ASTEROID_DY)
        #     elif y <= 50:
        #         velocity = Point(constants.ASTEROID_DX, constants.ASTEROID_DY * -1)
        # elif x >= 750:
            
        #     if y >= 550:
        #         velocity = Point(constants.ASTEROID_DX * -1, constants.ASTEROID_DY)
        #     elif y <= 50:
        #         velocity = Point(constants.ASTEROID_DX * -1, constants.ASTEROID_DY *-1)
        
        # # else:
        # #     velocity = Point(constants.ASTEROID_DX, constants.ASTEROID_DY)
           
        velocity = Point(constants.ASTEROID_DX, constants.ASTEROID_DY)

        asteroid.set_velocity(velocity)
        return asteroid