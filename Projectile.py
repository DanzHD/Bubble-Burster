import pygame

from Bubble import Bubble


class Projectile(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.velocity = 10
        self.sprite = pygame.image.load("./Assets/lazer.png").convert_alpha()
        self.sprite = pygame.transform.rotate(self.sprite, 90)
        self.rect = self.sprite.get_rect(topleft = (self.x_pos, self.y_pos))

    def collide_bubble(self, bubble):

        return pygame.sprite.collide_rect(self, bubble)

    def update_position(self):
        self.y_pos -= self.velocity
        self.rect = self.sprite.get_rect(topleft = (self.x_pos, self.y_pos))


