import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.radius = 8
        self.width = self.radius*2
        self.height = self.radius*2
        self.center_x = game.width//2
        self.center_y = game.height//4
        self.change_x = random.choice([-1,1])
        self.change_y = -1
        self.speed = 5
        self.color = arcade.color.RED

    def move(self):
        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed

    def draw(self):
        arcade.draw_circle_filled(
            self.center_x, self.center_y, self.radius, self.color)