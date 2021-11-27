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
            mouse = pygame.mouse.get_pos()
            if LOGIN_BUTTON_X <= mouse[0] <= LOGIN_BUTTON_X + BUTTON_WIDTH and \
                    LOGIN_BUTTON_Y <= mouse[1] <= LOGIN_BUTTON_Y + BUTTON_HEIGHT:
                print("hit login button")
            elif EXIT_BUTTON_X <= mouse[0] <= EXIT_BUTTON_X + BUTTON_WIDTH and \
                    EXIT_BUTTON_Y <= mouse[1] <= EXIT_BUTTON_Y + BUTTON_HEIGHT:
                pygame.quit()
                exit()


def draw(screen):
    screen.fill((0, 0, 0))

    button = Button(screen)
    button.draw_button(BUTTON_WIDTH, BUTTON_HEIGHT, LOGIN_BUTTON_X, LOGIN_BUTTON_Y, "Login", "Comic Sans MS")
    button.draw_button(BUTTON_WIDTH, BUTTON_HEIGHT, EXIT_BUTTON_X, EXIT_BUTTON_Y, "Exit", "Comic Sans MS")

    pygame.display.flip()


def create_screen():
    pygame.init()

    fps = 60
    dt = 1 / fps
    fps_clock = pygame.time.Clock()

    screen = pygame.display.set_mode((640, 480))

    while True:
        update(dt)
        draw(screen)

        dt = fps_clock.tick()


if __name__ == "__main__":
    create_screen()
