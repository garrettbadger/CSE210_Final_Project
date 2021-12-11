from game.action import Action
from game.actor import Actor
from game.point import Point

class GameOverAction(Action):
    def __init__(self, output_service):
        super().__init__()
        self._output_service = output_service
        self.play_again = Actor()
        self.exit = Actor()

    def execute(self, cast):
        
        game_over = Actor()
        game_over.set_height(200)
        game_over.set_width(200)
        game_over.set_text('Game Over! Better Luck Next Time!')
        game_over.set_position(Point(400, 300))
        self._output_service.draw_actor(game_over)

        
    # def create_play_again(self):
        self.play_again.set_width(125)
        self.play_again.set_height(125)
        self.play_again.set_text("Play again.")
        self.play_again.set_position(Point(100, 300))
        self._output_service.draw_box(100, 300, 125, 125)
        self._output_service.draw_actor(self.play_again)
        # return self.play_again

    # def create_exit(self):    
        self.exit.set_height(125)
        self.exit.set_width(125)
        self.exit.set_text("Exit")
        self.exit.set_position(Point(250, 300))
        self._output_service.draw_box(250, 300, 125, 125)
        self._output_service.draw_actor(self.exit)
        # return self.exit

