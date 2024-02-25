import pygame

pygame.init()

infoObject = pygame.display.Info()

screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
clock = pygame.time.Clock()
running = True

rect_1 = pygame.Rect(200, 100, 150, 100)

map_background = pygame.image.load("./Assets/background.jpg")
map_background = pygame.transform.scale(map_background, (infoObject.current_w, infoObject.current_h))

while running:
    screen.blit(map_background, (0, 0))
    pygame.draw.rect(screen, (255, 0, 255), rect_1)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
