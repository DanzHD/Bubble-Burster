import pygame

from Config import Config
from Bubble import Bubble
from Shooter import Shooter

screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))


def main():
    clock = pygame.time.Clock()
    running = True

    player_1_bubble = Bubble(0, 0)
    player_2_shooter = Shooter(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT - 200)

    map_background = pygame.image.load("./Assets/background.jpg")
    map_background = pygame.transform.scale(map_background, (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

    while running:
        screen.blit(map_background, (0, 0))

        screen.blit(player_1_bubble.sprite, (player_1_bubble.x_pos, player_1_bubble.y_pos))
        screen.blit(player_2_shooter.sprite, (player_2_shooter.x_pos, player_2_shooter.y_pos))

        key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        for projectile in player_2_shooter.projectiles.copy():
            if projectile.y_pos > -50:
                screen.blit(projectile.sprite, (projectile.x_pos, projectile.y_pos))
                projectile.update_position()
            else:
                player_2_shooter.projectiles.remove(projectile)
            if projectile.collide_bubble(player_1_bubble):
                game_over()
                running = False
                break

        player_1_bubble.handle_movement(key)
        player_2_shooter.handle_controls(key)

        pygame.display.flip()
        clock.tick(Config.FPS)

    pygame.quit()


def game_over():
    time_lasted = str(pygame.time.get_ticks() / 1000)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            break


        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('GameOver', True, (255, 255, 255))
        start_button = font.render('Bubble lasted: ' + time_lasted + " Seconds", True, (255, 255, 255))
        screen.blit(title, (
            Config.SCREEN_WIDTH / 2 - title.get_width() / 2, Config.SCREEN_HEIGHT / 2 - title.get_height() / 2))
        screen.blit(start_button,
                    (Config.SCREEN_WIDTH / 2 - start_button.get_width() / 2,
                     Config.SCREEN_HEIGHT / 2 + start_button.get_height() / 2))
        pygame.display.update()
        pygame.display.flip()


if __name__ == "__main__":
    main()
