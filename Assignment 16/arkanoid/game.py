import arcade
import ball
import paddle

WINDOW_SIZE_WIDTH = 600
WINDOW_SIZE_HEIGHT = 600

class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT, title="Arkanoid v1🤖")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.ball=ball.Ball()
        self.me=paddle.Paddle()


    def on_draw(self):
        arcade.start_render()

        arcade.finish_render()