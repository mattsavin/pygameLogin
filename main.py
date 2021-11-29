import pygame.locals
from button import *

LOGIN_BUTTON_X = 100
LOGIN_BUTTON_Y = 300
EXIT_BUTTON_X = 300
EXIT_BUTTON_Y = 300
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50


def update(dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass


def draw(screen):
    screen.fill((0, 0, 0))

    login_button = Button((50, 50, 100), LOGIN_BUTTON_X, LOGIN_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, "Login")
    exit_button = Button((50, 50, 100), EXIT_BUTTON_X, EXIT_BUTTON_Y, BUTTON_WIDTH, BUTTON_HEIGHT, "Exit")

    if login_button.is_hovering(pygame.mouse.get_pos()):
        print("hover!")
    login_button.draw(screen)
    exit_button.draw(screen)

    pygame.display.flip()


def create_screen():
    pygame.init()

    fps = 60
    dt = 1 / fps
    fps_clock = pygame.time.Clock()

    screen = pygame.display.set_mode((640, 480))

    while True:
        draw(screen)
        update(dt, )

        dt = fps_clock.tick()


if __name__ == "__main__":
    create_screen()
