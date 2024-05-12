import arcade
import food
import snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = snake.Snake(self)
        self.food = food.Apple(self)

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        arcade.draw_text("score: "+f"{self.snake.score}", self.width-50, self.height//50, arcade.color.BLACK, font_size=12, anchor_x="center")

        self.food.draw()
        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

    def on_update(self, delta_time: float):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)
            self.food = food.Apple(self)
