
from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point


class GameOverAction(Action):
    def __init__(self, output_service, audio_service):
        super().__init__()
        self._output_service = output_service
        self.play_again = Actor()
        self.exit = Actor()
        self._audio_service = audio_service
    def execute(self, cast):
        


        game_over = Actor()
        game_over.set_height(200)
        game_over.set_width(200)
        game_over.set_text('Game Over! Better Luck Next Time!')
        game_over.set_position(Point(200, 200))
        self._audio_service.play_sound(constants.SOUND_OVER)
        self._output_service.draw_actor(game_over)

        
    
