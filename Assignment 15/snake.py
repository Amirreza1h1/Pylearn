import arcade
import arcade.color
import arcade.color


class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 28
        self.height = 28
        self.center_x = game.width//2
        self.center_y = game.height//2
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 1
        self.body = []
        self.body_size = 0
        self.color1 = arcade.color.RED
        self.color2 = arcade.color.GREEN

    def draw(self):
        for i, part in enumerate(self.body):
            if i % 2 == 0:
                arcade.draw_rectangle_filled(
                    part['x'], part['y'], self.width, self.height, self.color2)
            else:
                arcade.draw_rectangle_filled(
                    part['x'], part['y'], self.width, self.height, self.color1)
            i += 1

        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, arcade.color.BLUE)

    def move(self):
        if self.change_x != 0:
            if self.change_x == 1:
                self.body.append({'x': self.center_x, 'y': self.center_y})
            if self.change_x == -1:
                self.body.append({'x': self.center_x, 'y': self.center_y})
        elif self.change_y != 0:
            if self.change_y == 1:
                self.body.append({'x': self.center_x, 'y': self.center_y})
            if self.change_y == -1:
                self.body.append({'x': self.center_x, 'y': self.center_y})

        if len(self.body) > self.body_size:
            self.body.pop(0)

        self.center_x += self.change_x*self.speed
        self.center_y += self.change_y*self.speed

    def eat(self, food):
        score = food.score
        del food
        self.score += score
        self.body_size += 1
