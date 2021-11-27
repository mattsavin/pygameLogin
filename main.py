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


if __name__ == "__main__":
    pygame.init()

    fps = 60
    fpsClock = pygame.time.Clock()

    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    dt = 1 / fps
    while True:
        update(dt)
        draw(screen)

        dt = fpsClock.tick()

