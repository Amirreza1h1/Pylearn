import arcade


class Raquette(arcade.Sprite):
    def __init__(self, x, y, n, c):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.name = n
        self.color = c
        self.change_x = 0
        self.change_y = 0
        self.width = 10
        self.height = 70
        self.speed = 4
        self.score = 0

    def move(self):
        ...

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)
