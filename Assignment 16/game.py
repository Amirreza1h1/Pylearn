import arcade
import raquette
import ball

WINDOW_SIZE_WIDTH = 1200
WINDOW_SIZE_HEIGHT = 700


class Game(arcade.Window):
    def __init__(self):
        super().__init__(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT, title="Pong 1 🏓")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.Player_1 = raquette.Raquette(
            40, self.height//2, "Amirreza", arcade.color.RED)
        self.Player_2 = raquette.Raquette(
            self.width-40, self.height//2, "Mamad", arcade.color.GREEN)
        self.ball = ball.Ball(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_outline(
            self.width//2, self.height//2, self.width-30, self.height-30, arcade.color.WHITE, 10)
        arcade.draw_line(self.width//2, 30, self.width//2,
                         self.height-30, arcade.color.WHITE, 10)
        self.Player_1.draw()
        self.Player_2.draw()
        self.ball.draw()
        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.Player_1.height < y < self.height-self.Player_1.height:
            self.Player_1.center_y = y

    def on_update(self, delta_time: float):
        self.ball.move()
        if self.ball.center_y<30 or self.ball.center_y>self.height-30:
            self.ball.change_y*=-1
