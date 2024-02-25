import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos

