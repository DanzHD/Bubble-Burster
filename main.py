import pygame

from Bubble import Bubble

pygame.init()

infoObject = pygame.display.Info()

screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
clock = pygame.time.Clock()
running = True

player_1_bubble = Bubble(0, 0)

map_background = pygame.image.load("./Assets/background.jpg")
map_background = pygame.transform.scale(map_background, (infoObject.current_w, infoObject.current_h))

while running:
    screen.blit(map_background, (0, 0))

    screen.blit(player_1_bubble.sprite, (player_1_bubble.x_pos, player_1_bubble.y_pos))

    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
        running = False
    player_1_bubble.handle_movement(key)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
