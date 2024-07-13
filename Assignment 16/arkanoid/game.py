import arcade
import ball
import paddle
import walls

WINDOW_SIZE_WIDTH = 600
WINDOW_SIZE_HEIGHT = 600


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT, title="Arkanoid v1🤖")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(
            ":resources:images/backgrounds/stars.png")
        self.life = 3
        self.heart_texture = arcade.load_texture(
            "heart.png")
        self.heart_x = 50
        self.ball = ball.Ball(self)
        self.me = paddle.Paddle(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(WINDOW_SIZE_WIDTH / 2, WINDOW_SIZE_HEIGHT / 2,
                                      WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT, self.background)
        self.me.draw()
        self.ball.draw()
        self.walls_list = [walls.Walls(self.width//2, self.height//2, arcade.color.RED, 1), walls.Walls(
            (self.width//2)+30, (self.height//2)+30, arcade.color.BLUE, 2), walls.Walls((self.width//2)+60, (self.height//2)+60, arcade.color.GREEN, 3)]

        for wall in self.walls_list:
            arcade.draw_rectangle_filled(
                wall.center_x, wall.center_y, wall.width, wall.height, wall.color)
        for i in range(self.life):
            arcade.draw_lrwh_rectangle_textured(
                (self.heart_x*i)+20, 10, 20, 20, self.heart_texture)
            arcade.draw_text(str(self.me.score), self.width - 40, 10,
                             arcade.color.WHITE, font_size=20, anchor_x="center")
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.me.width//2 < x < self.width-self.me.width//2:
            self.me.center_x = x

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.me.change_x = -1
        elif symbol == arcade.key.D:
            self.me.change_x = 1

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0


    def on_update(self, delta_time: float):
        self.ball.move()
        self.me.move()
        if arcade.check_for_collision(self.me, self.ball):
            self.ball.change_y *= -1

        if self.ball.center_x+8 > self.width:
            self.ball.change_x *= -1
        if self.ball.center_x-8 < 0:
            self.ball.change_x *= -1

        if self.ball.center_y+8 > self.height:
            self.ball.change_y *= -1

        if self.ball.center_y < 0:
            self.life -= 1
            del self.ball
            self.ball = ball.Ball(self)