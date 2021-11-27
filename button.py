import pygame


class Button:
    def __init__(self, screen):
        self.screen = screen

    def draw_button(self,  width, height, pos_x, pos_y, text, font):
        pygame.draw.rect(self.screen, [40, 50, 70], [pos_x, pos_y, width, height])
        pygame_font = pygame.font.SysFont(font, 35)
        pygame_text = pygame_font.render(text, True, (255, 255, 255))
        self.screen.blit(pygame_text, (pos_x + 10, pos_y))
