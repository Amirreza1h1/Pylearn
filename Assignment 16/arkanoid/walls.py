import random
import arcade

class Walls(arcade.Sprite):
    def __init__(self,x,y,color,score):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = 0
        self.width = 60
        self.height = 30
        self.color=color
        self.score=score