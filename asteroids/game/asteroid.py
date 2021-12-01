from game import constants
import random
from game.actor import Actor
from game.point import Point

class Asteroid(Actor):
    def __init__(self):
        super().__init__()
    
    def create_asteroid():
        x_list = []
        y_list = []
        asteroid = Asteroid()
        asteroid.set_height(random.randint(8, constants.ASTEROID_HEIGHT))
        asteroid.set_width(random.randint(8, constants.ASTEROID_WIDTH))
        top_x = random.randint(750, 800)
        x_list.append(top_x)
        bottom_x = random.randint(0, 50)
        x_list.append(bottom_x)
        top_y = random.randint(550, 600)
        y_list.append(top_y)
        bottom_y = random.randint(0, 50)
        y_list.append(bottom_y)
        x = random.choice(x_list)
        y = random.choice(y_list)
        position = Point(x, y)
        asteroid.set_position(position)
        if x <= 50:
            
            if y >= 550:
                velocity = Point(constants.ASTEROID_DX , constants.ASTEROID_DY)
            elif y <= 50:
                velocity = Point(constants.ASTEROID_DX, constants.ASTEROID_DY * -1)
        elif x >= 750:
            
            if y >= 550:
                velocity = Point(constants.ASTEROID_DX * -1, constants.ASTEROID_DY)
            elif y <= 50:
                velocity = Point(constants.ASTEROID_DX * -1, constants.ASTEROID_DY *-1)
        
        # else:
        #     velocity = Point(constants.ASTEROID_DX, constants.ASTEROID_DY)
           

        asteroid.set_velocity(velocity)
        return asteroid