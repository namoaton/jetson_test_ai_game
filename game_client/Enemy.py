import pygame
import os
from Spritesheet import SpriteSheet

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        player_img = pygame.image.load(os.path.join(img_folder, 'enemy.png')).convert()
        player_img = pygame.transform.rotate(player_img, 180)
        player_img = pygame.transform.scale(player_img, (50, 50))
        self.image = player_img
        transColor = self.image.get_at((0, 0))
        self.image.set_colorkey(transColor)
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos + 25, y_pos)
        self.on_screen = True
        self.is_hit = False
        self.blast_images = SpriteSheet(img_folder + "/explosion.png")
        self.blast_animation_step = 0

    def set_position(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos

    def get_position(self):
        return self.rect.x, self.rect.y

    def is_on_screen(self):
        return self.on_screen

    def launch(self, x_pos, y_pos):
        if self.on_screen:
            return Enemy(x_pos, y_pos)
        # self.on_screen = True
        # self.set_position(x_pos, y_pos)

    def update(self):
        if not self.is_hit:
            return
        self.image = self.blast_images.image_at(
            (self.blast_animation_step * 32, 0, 32, 32), )
        transColor = self.image.get_at((0, 0))
        self.image.set_colorkey(transColor)
        self.blast_animation_step += 1
        if self.blast_animation_step == 8:
            self.blast_animation_step = 0
            self.is_hit = False
            self.on_screen = False
