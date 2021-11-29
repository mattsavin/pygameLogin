import pygame.locals
from button import *


def update(dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            return event


def draw(screen, event):
    screen.fill((0, 0, 0))

    login_button = Button((50, 50, 100), 100, 300, 150, 50, "Login")
    exit_button = Button((50, 50, 100), 300, 300, 150, 50, "Exit")

    if login_button.is_hovering(pygame.mouse.get_pos()) and event and event.type == pygame.MOUSEBUTTONDOWN:
        print("login")
    elif exit_button.is_hovering(pygame.mouse.get_pos()) and event and event.type == pygame.MOUSEBUTTONDOWN:
        pygame.quit()
        exit()

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
        event = update(dt)
        draw(screen, event)

        dt = fps_clock.tick(fps)


if __name__ == "__main__":
    create_screen()
