import random

import pygame

class Wall:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.walls = []

    def add_wall(self, snake):
        x = random.randint(0, 480)
        y = random.randint(0, 480)
        # check if the wall is not colliding with the snake
        for i in snake.body:
            # get the rect of the snake
            rect = pygame.Rect(i[0], i[1], snake.width, snake.width)
            if rect.collidepoint(x, y):
                x = random.randint(0, 480)
                y = random.randint(0, 480)
        # check if the wall is not colliding with the other walls
        for i in self.walls:
            # get the rect of the wall
            rect = pygame.Rect(i[0], i[1], self.width, self.height)
            if rect.collidepoint(x, y):
                x = random.randint(0, 480)
                y = random.randint(0, 480)
        self.walls.append((x, y))

    def draw(self):
        for i in self.walls:
            pygame.draw.rect(self.screen, (255, 255, 255), (i[0], i[1], self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def detect_collision(self, snake):
        for i in self.walls:
            # get the rect of the wall
            rect = pygame.Rect(i[0], i[1], self.width, self.height)
            if rect.colliderect(snake.get_rect()):
                return True
        return False

    def reset(self):
        self.walls = []
