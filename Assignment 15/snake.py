import arcade

snake_color=1
class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.color = arcade.color.BLUE
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 1
        self.body = []

    def draw(self):
        global snake_color
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)

        for part in self.body:
            if snake_color==1:
                arcade.draw_rectangle_filled(
                part['x'], part['y'], self.width, self.height, arcade.color.GREEN)
                snake_color+=1
            else:
                arcade.draw_rectangle_filled(
                part['x'], part['y'], self.width, self.height, arcade.color.RED)
                snake_color-=1

    def move(self):
        self.body.append({'x': self.center_x, 'y': self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed

    def eat(self, food):
        score=food.score
        del food
        self.score+=score