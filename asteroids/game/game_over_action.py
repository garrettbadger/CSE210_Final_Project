from game.action import Action
from game.actor import Actor
from game.point import Point

class GameOverAction(Action):
    def __init__(self, output_service):
        super().__init__()
        self._output_service = output_service

    def execute(self, cast):
        
        game_over = Actor()
        game_over.set_height(200)
        game_over.set_width(200)
        game_over.set_text('Game Over! Better Luck Next Time!')
        game_over.set_position(Point(400, 300))
        self._output_service.draw_actor(game_over)

        play_again = Actor()
        play_again.set_height(150)
        play_again.set_width(150)
        play_again.set_text("Play again.")
        play_again.set_position(Point(100, 300))
        self._output_service.draw_box(100, 300, 150, 150)
        self._output_service.draw_actor(play_again)

