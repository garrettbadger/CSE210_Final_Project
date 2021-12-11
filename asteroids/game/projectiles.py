from game.actor import Actor
from game import constants
from game.point import Point
from game.ship import Ship

class Projectiles(Actor):
    def __init__(self):
        super().__init__()
    def create_projectile():
        projectile = Projectiles()
        projectile.set_height(constants.PROJECTILE_HEIGHT)
        projectile.set_width(constants.PROJECTILE_WIDTH)
        projectile.set_text('^')
        projectile.set_velocity(Point(constants.PROJECTILE_DX, constants.PROJECTILE_DY))
   
        return projectile


    