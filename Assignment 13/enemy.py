import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height+40
        self.width = 60
        self.height = 60
        self.angle = 180
        self.speed = 4
