import random
import time
import arcade
import arcade.key
import arcade.key
import spaceship
import enemy

ink =2

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=700, title="Spaceship Game 2024")
        # arcade.set_background_color(arcade.color.BLACK)
        self.game_over = False
        self.life = 3
        self.score = 0
        self.heart_texture = arcade.load_texture(
            ":resources:images/space_shooter/playerShip1_green.png")
        self.heart_x = 50
        self.background = arcade.load_texture(
            ":resources:images/backgrounds/stars.png")
        self.me = spaceship.Spaceship(self, "Amirreza")
        self.enemies = []
        self.last_enemy_spawn_time=0

    def on_draw(self):
        arcade.start_render()
        if self.game_over:
            arcade.draw_text("): Game Over :(", self.width // 2, self.height // 2,
                             color=arcade.color.RED, font_size=70, anchor_x="center")
            # arcade.draw_Text("Game Over", self.width // 2, self.height // 2,
            #             color=arcade.color.WHITE, font_size=20, anchor_x="center")
            arcade.draw_text("Your score: "+f"{self.score}", self.width//2, self.height //
                             3, arcade.color.WHITE, font_size=30, anchor_x="center")

        else:
            arcade.draw_lrwh_rectangle_textured(
                0, 0, 1000, 1000, self.background)
            self.me.draw()
            for emy in self.enemies:
                emy.draw()
            for bullet in self.me.bullet_list:
                bullet.draw()
            for i in range(self.life):
                arcade.draw_lrwh_rectangle_textured(
                    (self.heart_x*i)+50, 20, 50, 50, self.heart_texture, 0, 128)
            arcade.draw_text(str(self.score), self.width - 40, 40,
                             arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.me.change_x = -1
        elif symbol == arcade.key.D:
            self.me.change_x = 1
        if symbol == arcade.key.SPACE:
            self.me.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        self.me.change_x = 0

    def on_update(self, delta_time: float):
        global ink

        self.me.move()
        if self.game_over:
            time.sleep(5)
            exit(0)

        for em in self.enemies:
            if arcade.check_for_collision(self.me, em):
                self.game_over = True
                arcade.play_sound(arcade.sound.load_sound(
                    ":resources:sounds/explosion1.wav"))
            elif em.center_y < self.height//6:
                arcade.play_sound(arcade.sound.load_sound(
                    ":resources:sounds/explosion1.wav"))
                self.enemies.remove(em)
                if self.life > 0:
                    self.life -= 1
                else:
                    self.game_over = True
                    

        for em in self.enemies:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(em, bullet):
                    self.enemies.remove(em)
                    self.me.bullet_list.remove(bullet)
                    self.score += 1
                    arcade.play_sound(arcade.sound.load_sound(
                        ":resources:sounds/explosion1.wav"))

        for emy in self.enemies:
            emy.move()

        for bullet in self.me.bullet_list:
            bullet.move()

        for bullet in self.me.bullet_list:
            if bullet.center_y > 1000:
                self.me.bullet_list.remove(bullet)

        for em in self.enemies:
            if em.center_y < 0:
                self.enemies.remove(em)

        current_time = time.time()
        if current_time - self.last_enemy_spawn_time >= 3:
            self.emy = enemy.Enemy(self,ink)
            ink=self.emy.enemy_speed()
            self.enemies.append(self.emy)
            self.last_enemy_spawn_time = current_time
            print(self.emy.speed)