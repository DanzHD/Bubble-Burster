import pygame


class Config:
    pygame.init()
    FPS = 60
    infoObject = pygame.display.Info()
    SCREEN_WIDTH = pygame.display.Info().current_w
    SCREEN_HEIGHT = pygame.display.Info().current_h


