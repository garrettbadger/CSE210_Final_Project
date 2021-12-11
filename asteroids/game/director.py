import random
from time import sleep

import raylibpy
from game.asteroid import Asteroid
from game.handle_off_screen_action import HandleOffScreenAction
from game import constants
from random import Random

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        # self.game = HandleOffScreenAction()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            score = self._cast['score'][0]

            # TODO: Add some logic like the following to handle game over conditions
            if len(self._cast['asteroids']) == 0:
                self._cue_action("gameover")
            elif len(self._cast['asteroids']) > 0:
                
        
                if score.get_score() < 25:
                    if len(self._cast['asteroids']) < 5:
                        asteroid = Asteroid.create_asteroid()
                        self._cast['asteroids'].append(asteroid)
                if score.get_score() > 25 < 50:
                    if len(self._cast['asteroids']) < 7:
                        asteroid = Asteroid.create_asteroid()
                        self._cast['asteroids'].append(asteroid)
                if score.get_score() > 50 < 75:
                    if len(self._cast['asteroids']) < 9:
                        asteroid = Asteroid.create_asteroid()
                        self._cast['asteroids'].append(asteroid)
                if score.get_score() > 75 < 100:
                    if len(self._cast['asteroids']) < 11:
                        asteroid = Asteroid.create_asteroid()
                        self._cast['asteroids'].append(asteroid)
                if score.get_score() > 100 < 125:
                    if len(self._cast['asteroids']) <13:
                        asteroid = Asteroid.create_asteroid()
                        self._cast['asteroids'].append(asteroid)

                if score.get_score() > 125 < 150:
                    if len(self._cast['asteroids']) < 15:
                        asteroid = Asteroid.create_asteroid()
                        self._cast['asteroids'].append(asteroid)

                if score.get_score() > 150 < 175:
                    if len(self._cast['asteroids']) < 17:
                        asteroid = Asteroid.create_asteroid()
                        self._cast['asteroids'].append(asteroid)
                    

            

        
            
                
                

            if raylibpy.window_should_close():
                self._keep_playing = False


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.

        """ 
        
        for action in self._script[tag]:
            action.execute(self._cast)

            