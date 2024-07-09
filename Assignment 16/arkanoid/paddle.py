import arcade


class Paddle(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x = game.width//2
        self.center_y = 50
        self.change_x = 0
        self.change_y = 0
        self.width = 70
        self.height = 10
        self.speed = 4
        self.color = arcade.color.BLUE
        self.score = 0

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)
        
    
