import arcade
import bullet


class Spaceship(arcade.Sprite):
    def __init__(self, game, name):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = game.width//2
        self.center_y = game.height//6
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.name = name
        self.speed = 6
        self.game = game
        self.bullet_list = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.game.width:
                self.center_x += self.speed

    def fire(self):
        new_bullet = bullet.Bullet(self)
        self.bullet_list.append(new_bullet)
        arcade.play_sound(arcade.sound.load_sound(":resources:sounds/laser1.wav"))
