
from game.action import Action
from game.actor import Actor
from game.point import Point
from game.director import Director
from game.asteroid import Asteroid

class GameOverAction(Action):
    def __init__(self, output_service, physics_service, script):
        super().__init__()
        self._output_service = output_service
        self.play_again = Actor()
        self.exit = Actor()
        self._physics_service = physics_service
        self._script = script

    def execute(self, cast):
        # projectiles = cast['projectiles']


        game_over = Actor()
        game_over.set_height(200)
        game_over.set_width(200)
        game_over.set_text('Game Over! Better Luck Next Time!')
        game_over.set_position(Point(200, 200))
        self._output_service.draw_actor(game_over)

        
    # def create_play_again(self):
        # self.play_again.set_width(125)
        # self.play_again.set_height(125)
        # self.play_again.set_text("Play again.")
        # self.play_again.set_position(Point(100, 300))
        # self._output_service.draw_box(100, 300, 125, 125)
        # self._output_service.draw_actor(self.play_again)
        # for projectile in projectiles:
        #     if self._physics_service.is_collision(projectile, self.play_again):
        #         self.play_again.set_height(0)
        #         self.play_again.set_width(0)
        #         self.play_again.set_text("")
        #         self.play_again.set_position(Point(0, 0))
        #         # self._output_service.flush_buffer()
        #         Asteroid.create_asteroid()
        #         director = Director(cast, self._script)
        #         director.start_game()
        # return self.play_again

    # def create_exit(self):    
        # self.exit.set_height(125)
        # self.exit.set_width(125)
        # self.exit.set_text("Exit")
        # self.exit.set_position(Point(250, 300))
        # self._output_service.draw_box(250, 300, 125, 125)
        # self._output_service.draw_actor(self.exit)
        # for projectile in projectiles:
        #     if self._physics_service.is_collision(projectile, self.exit):
        #         self.exit.set_height(0)
        #         self.exit.set_width(0)
        #         self.exit.set_text("")
        #         self.exit.set_position(Point(0, 0))
        #         self._output_service.draw_box(0, 0, 0, 0)
        # return self.exit

