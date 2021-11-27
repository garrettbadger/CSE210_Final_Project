from game.action import Action
from game import constants
from game.point import Point

class HandleOffScreenAction(Action):
    def __init__(self) -> None:
        super().__init__()
        self.game_over = False
        
    

    def execute(self, cast):
        ball = cast['balls'][0]
        for group in cast:
            if group == 'balls':
                position = ball.get_position()
                velocity = ball.get_velocity()
                # if position.get_x() >= constants.MAX_X:
                #     ball.set_velocity(Point((velocity.get_x() * -1), velocity.get_y()))
                    
                # elif position.get_y() >= constants.MAX_Y:
                #     ball.set_velocity(Point(velocity.get_x(), (velocity.get_y() * -1)))
                if ball.get_top_edge() <= 0 or ball.get_bottom_edge() >= constants.MAX_Y:
                    ball.set_velocity(Point(velocity.get_x(), (velocity.get_y() * -1)))
                elif ball.get_right_edge() >= constants.MAX_X or ball.get_left_edge() <= 0:
                    ball.set_velocity(Point((velocity.get_x() * -1), velocity.get_y()))
                
                if ball.get_bottom_edge() >= constants.MAX_Y:
                    ball.remove(ball)

        
    
                       
                


