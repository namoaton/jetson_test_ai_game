import pygame
import os
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WIDTH = 640
HEIGHT = 480


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        player_img = pygame.image.load(os.path.join(img_folder, 'Ship_Icon.png')).convert()
        player_img = pygame.transform.scale(player_img, (50, 50))
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 30)


    def move_left(self):
        self.rect.x -= 5
        if self.rect.x < 0:
            self.rect.x = 0

    def move_right(self):
        self.rect.x += 5
        if self.rect.x > WIDTH - 50:
            self.rect.x = WIDTH - 50

    def get_position(self):
        return self.rect.x, self.rect.y

    def update(self):
        pass
        # self.rect.x += 5
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0

