import random
import arcade

class Walls(arcade.Sprite):
    def __init__(self,color,score):
        super().__init__()
        self.center_x
        self.center_y
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 25
        self.color=color
        self.score=score