import pygame
import random


class Food:
    def __init__(self, screen, width, max_x, max_y):
        self.screen = screen
        self.x = random.randint(0, 480)
        self.y = random.randint(0, 480)
        self.width = width
        self.max_x = max_x
        self.max_y = max_y
        self.x_direction = 0
        self.y_direction = 0

    def draw(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.x, self.y, self.width, self.width))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.width)

    def spawn_food(self, snake, wall):
        x = random.randint(0, 480)
        y = random.randint(0, 480)
        self.x_direction = random.randint(0, 2)
        if self.x_direction == 0:
            self.y_direction = random.randint(1, 2)
        else:
            self.y_direction = random.randint(0, 2)

        # check if the food is not colliding with the snake
        for i in snake.body:
            # get the rect of the snake
            rect = pygame.Rect(i[0], i[1], snake.width, snake.width)
            if rect.collidepoint(x, y):
                x = random.randint(0, 480)
                y = random.randint(0, 480)

        # check if the food is not colliding with the walls
        for i in wall.walls:
            # get the rect of the wall
            rect = pygame.Rect(i[0], i[1], wall.width, wall.height)
            if rect.collidepoint(x, y):
                x = random.randint(0, 480)
                y = random.randint(0, 480)

        self.x = x
        self.y = y

    def reset(self):
        self.x = random.randint(0, 480)
        self.y = random.randint(0, 480)
        self.x_direction = random.randint(0, 2)
        if self.x_direction == 0:
            self.y_direction = random.randint(1, 2)
        else:
            self.y_direction = random.randint(0, 2)

    def move_food(self, wall, snake):
        # We define the direction x and y direction
        # x direction = 0 = none, 1 = left, 2 = right
        # y direction = 0 = none, 1 = up, 2 = down

        # We check if the food collides border and change
        if self.x <= 0:
            self.x_direction = 2
        elif self.x >= self.max_x:
            self.x_direction = 1

        if self.y <= 0:
            self.y_direction = 2
        elif self.y >= self.max_y:
            self.y_direction = 1

        # We check if the food collides a wall and change
        for i in wall.walls:
            # get the rect of the wall
            rect = pygame.Rect(i[0], i[1], wall.width, wall.height)
            if rect.colliderect(self.get_rect()):
                if self.x_direction == 1:
                    self.x_direction = 2
                elif self.x_direction == 2:
                    self.x_direction = 1
                elif self.y_direction == 1:
                    self.y_direction = 2
                elif self.y_direction == 2:
                    self.y_direction = 1

        # We check if the food collides the snake and change
        for i in snake.body:
            # get the rect of the snake
            rect = pygame.Rect(i[0], i[1], snake.width, snake.width)
            if rect.colliderect(self.get_rect()):
                if self.x_direction == 1:
                    self.x_direction = 2
                elif self.x_direction == 2:
                    self.x_direction = 1
                elif self.y_direction == 1:
                    self.y_direction = 2
                elif self.y_direction == 2:
                    self.y_direction = 1

        # We move the food
        if self.x_direction == 1:
            self.x -= self.width * 0.3
        elif self.x_direction == 2:
            self.x += self.width * 0.3
        if self.y_direction == 1:
            self.y -= self.width * 0.3
        elif self.y_direction == 2:
            self.y += self.width * 0.3

