import pygame
import pygame.locals


def update(dt):
    for event in pygame.event.get():

        if event.type == pygame.locals.QUIT:
            pygame.quit()
            exit()


def draw(screen):
    screen.fill((0, 0, 0))

    # Do cool stuff

    pygame.display.flip()


def create_screen():
    pygame.init()
    fps = 60
    dt = 1 / fps
    fps_clock = pygame.time.Clock()
    res = (640, 480)
    screen = pygame.display.set_mode(res)
    while True:
        update(dt)
        draw(screen)

        dt = fps_clock.tick()


if __name__ == "__main__":
    create_screen()
