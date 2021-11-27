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
        paddle = cast["paddle"][0] # there's only one
        ball = cast["balls"][0] # there's only one
        bricks = cast["bricks"]
        velocity = ball.get_velocity()
        if self._physics_service.is_collision(paddle, ball):
            ball.set_velocity(Point(velocity.get_x(), (velocity.get_y() * -1)))
            AudioService().play_sound(constants.SOUND_BOUNCE)


        
        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                ball.set_velocity(Point(velocity.get_x(), (velocity.get_y() * -1)))
                bricks.remove(brick)
                AudioService().play_sound(constants.SOUND_BOUNCE)

                 