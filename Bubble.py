from Config import Config
from Player import Player
import pygame


class Bubble(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.speed = 5
        self.sprite = pygame.image.load("./Assets/bubble_1.png").convert_alpha()
        self.rect = self.sprite.get_rect(topleft = (self.x_pos, self.y_pos))

    def handle_movement(self, key):
        if key[pygame.K_DOWN]:
            self.y_pos += self.speed
            if self.y_pos > Config.SCREEN_HEIGHT - 200:
                self.y_pos -= self.speed

        if key[pygame.K_UP]:
            self.y_pos -= self.speed
            if self.y_pos < 0:
                self.y_pos += self.speed
        if key[pygame.K_LEFT]:
            self.x_pos -= self.speed
            if self.x_pos < 0:
                self.x_pos += self.speed
        if key[pygame.K_RIGHT]:
            self.x_pos += self.speed
            if self.x_pos > Config.SCREEN_WIDTH - 50:
                self.x_pos -= self.speed
        self.rect = self.sprite.get_rect(topleft = (self.x_pos, self.y_pos))
