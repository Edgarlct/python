import pygame


class Message:
    def __init__(self, screen):
        self.screen = screen
        self.text = ""
        self.x = 10
        self.y = 50
        self.color = (255, 0, 0)

    def draw(self):
        font = pygame.font.SysFont("arial", 16)
        text = font.render(self.text, True, self.color)
        self.screen.blit(text, (self.x, self.y))

    def set_text(self, text):
        self.text = text

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
