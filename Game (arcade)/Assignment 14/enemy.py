import random
import arcade


class Enemy(arcade.Sprite):
    def __init__(self, game, increment):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height+40
        self.width = 60
        self.height = 60
        self.angle = 180
        self.speed = increment

    def move(self):
        self.center_y -= self.speed

    def enemy_speed(self):
        self.speed += 0.05
        return self.speed
