import pygame
import os

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480


class Missile(pygame.sprite.Sprite):
    def __init__(self,x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        player_img = pygame.image.load(os.path.join(img_folder, 'missile.png')).convert()
        # player_img = pygame.transform.scale(player_img, (50, 50))
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos+25, y_pos)
        self.on_screen = True

    def set_position(self, x_pos, y_pos):
        self.rect.x = x_pos
        self.rect.y = y_pos

    def get_position(self):
        return self.rect.x, self.rect.y

    def is_on_screen(self):
        return self.on_screen

    def launch(self, x_pos, y_pos):
        if self.on_screen:
            return Missile(x_pos,y_pos)
        # self.on_screen = True
        # self.set_position(x_pos, y_pos)

    def explode(self):
        self.on_screen = False

    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.on_screen = False
