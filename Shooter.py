from Player import Player
import pygame

from Projectile import Projectile
from Config import Config


class Shooter(Player):

    TIME_BETWEEN_SHOTS = 600

    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.sprite = pygame.image.load("./Assets/staff.png").convert_alpha()
        self.projectiles = []
        self.previous_shot = -self.TIME_BETWEEN_SHOTS
        self.current_shot = pygame.time.get_ticks()
        self.speed = 7

    def handle_controls(self, key):
        if key[pygame.K_a]:
            self.x_pos -= self.speed
            if self.x_pos < -50:
                self.x_pos += self.speed
        if key[pygame.K_d]:
            self.x_pos += self.speed
            if self.x_pos > Config.SCREEN_WIDTH - 200:
                self.x_pos -= self.speed

        if key[pygame.K_SPACE]:
            self.current_shot = pygame.time.get_ticks()

            if (self.current_shot - self.previous_shot) > self.TIME_BETWEEN_SHOTS:
                self.previous_shot = pygame.time.get_ticks()
                self.projectiles.append(Projectile(self.x_pos + 50, self.y_pos))
