import arcade

class Snake(arcade.Sprite):
    def __init__(self,game):
        super().__init__()
        self.width=32
        self.height=32
        self.center_x=game.width//2
        self.center_y=game.height//2
        self.color=arcade.color.BLUE
        self.change_x=0
        self.change_y=0
        self.speed=4
        self.score=0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

    def move(self):
        self.center_x+=self.change_x*self.speed
        self.center_y+=self.change_y*self.speed

    def eat(self,food):
        del food.food
        self.score+=1