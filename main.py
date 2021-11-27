import pygame.locals
from button import *


def update():
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
    button.draw_button(50, 50, 140, 40, "Hello", "Comic Sans MS")

    pygame.display.flip()


def create_screen():
    pygame.init()

    fps = 60
    dt = 1 / fps
    fps_clock = pygame.time.Clock()
    dt = fps_clock.tick()

    res = (640, 480)
    screen = pygame.display.set_mode(res)

    while True:
        update()
        draw(screen)


if __name__ == "__main__":
    create_screen()
