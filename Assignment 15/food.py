import random
import arcade


class Food(arcade.Sprite):
    def __ini__(self,game,picture):
        super().__init__(picture)
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, game.width-10)
        self.center_y = random.randint(10, game.height-10)
        self.change_x = 0
        self.change_y = 0


class Apple(Food):
    def __init__(self, game):
        super().__init__(game,'apple.png')
        # self.width = 32
        # self.height = 32
        # self.center_x = random.randint(10, game.width-10)
        # self.center_y = random.randint(10, game.height-10)
        # self.change_x = 0
        # self.change_y = 0

class Banana(Food):
    def __init__(self,game):
        super().__init__(game,'banana.png')