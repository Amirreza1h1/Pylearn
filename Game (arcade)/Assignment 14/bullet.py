import arcade
import spaceship


class Bullet(arcade.Sprite):
    def __init__(self, host):
        super().__init__(":resources:images/space_shooter/laserBlue01.png")
        self.angle = -90
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 3
        self.change_x = 0
        self.change_y = 1
        self.scale = 0.5

    def move(self):
        self.center_y += self.speed
