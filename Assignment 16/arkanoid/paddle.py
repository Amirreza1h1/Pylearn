import arcade

class Paddle(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0
        self.width = 60
        self.height = 40
        self.speed = 4
        self.score = 0 