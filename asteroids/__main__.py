import os



os.environ['RAYLIB_BIN_PATH'] = r'D:\cse210-student-solo-checkpoints\raylib-2.0.0-Win64-mingw\lib'
import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.asteroid import Asteroid
from game.projectiles import Projectiles
from game.move_actors_action import MoveActorsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.ship import Ship
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.game_over import GameOver
from game.game_over_action import GameOverAction
from game.score import Score

# TODO: Add imports similar to the following when you create these classes



def main():

    # create the cast {key: tag, value: list}
    cast = {}

    
    # TODO: Create bricks here and add them to the list
    
    asteroids = []
    for i in range(5):
        asteroid = Asteroid.create_asteroid()
        asteroids.append(asteroid)
    cast['asteroids'] = asteroids

          

    # cast["balls"] = []
    # TODO: Create a ball here and add it to the list
    projectiles = []
      
    
    
    cast['projectiles'] = projectiles

    
    # TODO: Create a paddle here and add it to the list
    ships = []
    ship = Ship()
    ship.set_height(constants.SHIP_HEIGHT)
    ship.set_width(constants.SHIP_WIDTH)
    ship.set_position(Point(constants.MAX_X/2, constants.MAX_Y/2))
    ship.set_image(r"asteroids\assets\pitrizzo-SpaceShip-gpl3-opengameart-24x24.png")
    ships.append(ship)
    

    cast["ship"] = ships

    
    
    cast["messages"] = ""

    scores = []
    score = Score()
    score.set_height(50)
    score.set_width(50)
    score.set_position(Point(10, 10))
    score.set_text('0' )
    scores.append(score)

    cast['score'] = scores


    # Create the script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()

    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)
    game_over_action = GameOverAction(output_service, audio_service)
    # TODO: Create additional actions here and add them to the script

    script["input"] = []
    script["update"] = [move_actors_action, control_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]
    script["gameover"] = [game_over_action]


  
    # Start the game
    output_service.open_window("Asteroids")  
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game()
 
    audio_service.stop_audio()

if __name__ == "__main__":
     main()


 