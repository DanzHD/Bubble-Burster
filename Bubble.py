from Player import Player
import pygame


class Bubble(Player):

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.sprite = pygame.image.load("./Assets/bubble_1.png").convert_alpha()

    def handle_movement(self, key):
        if key[pygame.K_DOWN]:
            self.y_pos += 3
        if key[pygame.K_UP]:
            self.y_pos -= 3
        if key[pygame.K_LEFT]:
            self.x_pos -= 3
        if key[pygame.K_RIGHT]:
            self.x_pos += 3
