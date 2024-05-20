import arcade
import food
import snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = snake.Snake(self)
        self.food_1 = food.Apple(self)
        self.food_2 = food.Banana(self)
        self.food_3=food.Poo(self)


    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        arcade.draw_text("score: "+f"{self.snake.score}", self.width-50, self.height//50, arcade.color.BLACK, font_size=12, anchor_x="center")

        self.food_1.draw()
        self.food_2.draw()
        self.food_3.draw()

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

        if arcade.check_for_collision(self.snake, self.food_1):
            self.snake.eat(self.food_1)
            self.food_1 = food.Apple(self)

        if arcade.check_for_collision(self.snake, self.food_2):
            self.snake.eat(self.food_2)
            self.food_2 = food.Banana(self)

        
        if arcade.check_for_collision(self.snake, self.food_3):
            self.snake.eat(self.food_3)
            self.food_3 = food.Poo(self)
        
        #game over needs modify
        while 1:
            if arcade.check_for_collision(self.snake,self.snake):
                print("game over!")
            if self.snake.center_x-32==0 or self.snake.center_x+32==500:
                print("game over!")
            if self.snake.center_y-32==0 or self.snake.center_y+32==500:
                print("game over!")
            if self.snake.score==0:
                print("game over!")
                