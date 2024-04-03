import arcade
import spaceship
import enemy


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=1000, title="Spaceship Game 2024")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(
            ":resources:images/backgrounds/stars.png")
        self.me = spaceship.Spaceship(self, "Amirreza")
        self.emy = enemy.Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1000, 1000, self.background)
        self.me.draw()
        self.emy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.me.center_x -= self.me.speed
        elif symbol == 100:
            self.me.center_x += self.me.speed

    def on_update(self, delta_time: float):
        self.emy.center_y -= self.emy.speed
