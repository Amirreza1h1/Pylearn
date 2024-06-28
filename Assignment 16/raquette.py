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

    def move(self, game, ball):
        if ball.center_x > game.width//2:

            if ball.center_y > self.center_y:
                self.change_y = 1
            if ball.center_y < self.center_y:
                self.change_y = -1
            self.center_y += self.change_y*self.speed
            if self.center_y > game.height-self.height:
                self.center_y = game.height-self.height
            if self.center_y < self.height:
                self.center_y = self.height

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)
