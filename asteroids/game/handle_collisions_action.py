import random

from game.audio_service import AudioService
from game import constants
from game.action import Action
from game.point import Point


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service
        
        

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ship = cast["ship"][0] 
        projectiles = cast["projectiles"]
        asteroids = cast["asteroids"]
        score = cast['score'][0]
        
        
        for asteroid in asteroids:
            if self._physics_service.is_collision(ship, asteroid):
                asteroids.clear()
                AudioService().play_sound(constants.SOUND_HIT)


        
        for projectile in projectiles:
            for asteroid in asteroids:
                if self._physics_service.is_collision(projectile, asteroid):
                    if asteroid.get_width() > 64 or asteroid.get_height() > 64:
                        asteroid.set_width(asteroid.get_width() - 1)
                        asteroid.set_height(asteroid.get_height() -1)
                        if len(projectiles) > 0:
                            projectiles.remove(projectile)
                            break
                    elif asteroid.get_width() > 63 or asteroid.get_height() > 63:
                        asteroid.set_width(asteroid.get_width() - 1)
                        asteroid.set_height(asteroid.get_height() -1)
                        if len(projectiles) > 0:
                            projectiles.remove(projectile)
                            break
                    elif asteroid.get_width() > 62 or asteroid.get_height() > 62:
                        asteroid.set_width(asteroid.get_width() - 1)
                        asteroid.set_height(asteroid.get_height() -1)
                        if len(projectiles) > 0:
                            projectiles.remove(projectile)
                            break
                    
                    if asteroid.get_width() <= 62 or asteroid.get_height() <= 62:                  
                        asteroids.remove(asteroid)
                        score.set_score(1)
                        
                        score.set_text(str(score.get_score()))
                        
                        AudioService().play_sound(constants.SOUND_HIT)

        