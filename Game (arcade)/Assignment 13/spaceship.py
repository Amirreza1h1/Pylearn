import arcade


class Spaceship(arcade.Sprite):
    def __init__(self, game, name):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width//2
        self.center_y = game.height//4
        self.width = 50
        self.height = 50
        self.name = name
        self.speed = 8
