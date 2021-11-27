import pygame.locals
from button import *


def update(dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if True:
                print("MOUSEBUTTONDOWN")


def draw(screen):
    screen.fill((0, 0, 0))

    button = Button(screen)
    button.draw_button(150, 50, 100, 50, "Hello", "Comic Sans MS")
    button.draw_button(150, 50, 300, 50, "Hello", "Comic Sans MS")

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
