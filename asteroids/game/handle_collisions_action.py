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
        ship = cast["ship"][0] # there's only one
        projectiles = cast["projectiles"]
        asteroids = cast["asteroids"]
        # velocity = ball.get_velocity()
        for asteroid in asteroids:
            if self._physics_service.is_collision(ship, asteroid):
                asteroids.clear()
                # AudioService().play_sound(constants.SOUND_BOUNCE)


        
        for projectile in projectiles:
            for asteroid in asteroids:
                if self._physics_service.is_collision(projectile, asteroid):
                    if asteroid.get_width() > 24 or asteroid.get_height() > 24:
                        
                        asteroid.set_width(asteroid.get_width() - 9)
                        asteroid.set_height(asteroid.get_height() -5)
                        projectiles.remove(projectile)
                    if asteroid.get_width() <= 23 or asteroid.get_height() <= 23:                  
                        asteroids.remove(asteroid)
                        # projectiles.remove(projectile)
                    # AudioService().play_sound(constants.SOUND_BOUNCE)

                 