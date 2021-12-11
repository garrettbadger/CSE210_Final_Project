from game.action import Action
from game import constants
from game.point import Point

class HandleOffScreenAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self.game_over = False
        
    

    def execute(self, cast):
        asteroid = cast['asteroids']
        ship = cast['ship'][0]
        for group in cast:
            if group == 'asteroids':
                for actor in cast['asteroids']:
               
                    if actor.get_top_edge() <= 0 or actor.get_bottom_edge() >= constants.MAX_Y:
                        asteroid.remove(actor)
                    elif actor.get_right_edge() >= constants.MAX_X or actor.get_left_edge() <= 0:
                        asteroid.remove(actor)
            
                    if actor.get_bottom_edge() >= constants.MAX_Y:
                        asteroid.clear()

        projectile = cast['projectiles']
        for group in cast:
            if group == 'projectiles':
                for actor in cast['projectiles']:
               
                    if actor.get_top_edge() <= 0 or actor.get_bottom_edge() >= constants.MAX_Y:
                        projectile.remove(actor)
                    elif actor.get_right_edge() >= constants.MAX_X or actor.get_left_edge() <= 0:
                        projectile.remove(actor)
                    
              
        if ship.get_right_edge() >= constants.MAX_X:
            ship.set_position(Point(ship.get_position().get_x()-15, ship.get_position().get_y()))
        if ship.get_left_edge() <= 20:
            ship.set_position(Point(ship.get_position().get_x()+15, ship.get_position().get_y()))
        if ship.get_bottom_edge() >= constants.MAX_Y:
            ship.set_position(Point(ship.get_position().get_x(), ship.get_position().get_y()-15))


            
        
    
                       
                


