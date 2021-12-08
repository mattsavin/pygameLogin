import pygame
import pygame.locals


class Button:
    def __init__(self, color, x, y, w, h, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.text = text

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('Comic Sans MS', 60)
            text = font.render(self.text, True, (0, 0, 0))
            win.blit(text,
                     (self.x + (self.width / 2 - text.get_width() / 2),
                      self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        else:
            return False


class TextInputBox(pygame.sprite.Sprite):
    def __init__(self, x, y, w, font):
        super().__init__()
        self.color = (255, 255, 255)
        self.backcolor = None
        self.pos = (x, y)
        self.width = w
        self.font = font
        self.active = False
        self.text = ""
        self.render_text()

    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width() + 10), t_surf.get_height() + 10),
                                    pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text()


def update(dt):
    for e in pygame.event.get():
        if e.type == pygame.locals.QUIT:
            pygame.quit()
            exit()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            return e


def draw(s, e):
    font = pygame.font.SysFont('Comic Sans MS', 60)
    s.fill((0, 0, 0))

    username_box = TextInputBox(50, 50, 400, font)
    # password_box = TextInputBox(50, 150, 400, font)

    group = pygame.sprite.Group(username_box)

    login_button = Button((50, 50, 100), 100, 300, 150, 50, "Login")
    exit_button = Button((50, 50, 100), 300, 300, 150, 50, "Exit")

    if login_button.is_over(pygame.mouse.get_pos()) and e and e.type == pygame.MOUSEBUTTONDOWN:
        print("login")
    elif exit_button.is_over(pygame.mouse.get_pos()) and e and e.type == pygame.MOUSEBUTTONDOWN:
        pygame.quit()
        exit()

    group.update(pygame.event.get())

    login_button.draw(screen)
    exit_button.draw(screen)

    group.draw(screen)

    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    fps = 60
    fpsClock = pygame.time.Clock()

    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    dt = 1 / fps
    while True:
        event = update(dt)
        draw(screen, event)

        dt = fpsClock.tick()
