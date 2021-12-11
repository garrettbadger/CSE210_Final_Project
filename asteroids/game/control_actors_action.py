
from game import constants
from game.action import Action
from game.projectiles import Projectiles
from game.point import Point


class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        score = cast['score'][0]
        direction = self._input_service.get_direction()
        ship = cast["ship"][0] # there's only one in the cast
        ship.set_velocity(direction.scale(constants.SHIP_SPEED))  

        projectile = self._input_service.get_projectile()
        if projectile == True:
            if score.get_score() >= 200:
                bullet1 = Projectiles.create_projectile()
                bullet2 = Projectiles.create_projectile()
                bullet3 = Projectiles.create_projectile()
                x1 = ship.get_position().get_x() - 5
                y1 = ship.get_position().get_y()
                x2 = ship.get_position().get_x() + 5
                bullet1.set_position(Point(x1, y1))
                bullet2.set_position(Point(x2, y1))
                bullet3.set_position(ship.get_position())
                bullet1.set_velocity(Point(constants.PROJECTILE_DX, constants.L3PROJECTILE_DY))
                bullet2.set_velocity(Point(constants.PROJECTILE_DX, constants.L3PROJECTILE_DY))
                bullet3.set_velocity(Point(constants.PROJECTILE_DX, constants.L3PROJECTILE_DY))
                

                cast['projectiles'].append(bullet1)
                cast['projectiles'].append(bullet2)
                cast['projectiles'].append(bullet3)
            elif score.get_score() >= 150:
                bullet1 = Projectiles.create_projectile()
                bullet2 = Projectiles.create_projectile()
                bullet3 = Projectiles.create_projectile()
                x1 = ship.get_position().get_x() - 5
                y1 = ship.get_position().get_y()
                x2 = ship.get_position().get_x() + 5
                bullet1.set_position(Point(x1, y1))
                bullet2.set_position(Point(x2, y1))
                bullet3.set_position(ship.get_position())
                bullet1.set_velocity(Point(constants.PROJECTILE_DX, constants.L2PROJECTILE_DY))
                bullet2.set_velocity(Point(constants.PROJECTILE_DX, constants.L2PROJECTILE_DY))
                bullet3.set_velocity(Point(constants.PROJECTILE_DX, constants.L2PROJECTILE_DY))

                cast['projectiles'].append(bullet1)
                cast['projectiles'].append(bullet2)
                cast['projectiles'].append(bullet3)
            elif score.get_score() >= 100 :
                bullet1 = Projectiles.create_projectile()
                bullet2 = Projectiles.create_projectile()
                x1 = ship.get_position().get_x() - 3
                y1 = ship.get_position().get_y()
                x2 = ship.get_position().get_x() + 3
                bullet1.set_position(Point(x1, y1))
                bullet2.set_position(Point(x2, y1))
                bullet1.set_velocity(Point(constants.PROJECTILE_DX, constants.L2PROJECTILE_DY))
                bullet2.set_velocity(Point(constants.PROJECTILE_DX, constants.L2PROJECTILE_DY))

                cast['projectiles'].append(bullet1)
                cast['projectiles'].append(bullet2)
            elif score.get_score() >= 50:
               
                bullet1 = Projectiles.create_projectile()
                bullet2 = Projectiles.create_projectile()
                x1 = ship.get_position().get_x() - 3
                y1 = ship.get_position().get_y()
                x2 = ship.get_position().get_x() + 3
                bullet1.set_position(Point(x1, y1))
                bullet2.set_position(Point(x2, y1))
               
                cast['projectiles'].append(bullet1)
                cast['projectiles'].append(bullet2)
            
            elif score.get_score() < 50:
                bullet = Projectiles.create_projectile()
                bullet.set_position(ship.get_position())
                cast['projectiles'].append(bullet)
                
            
            
            

            

