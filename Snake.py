import pygame
import random


class Snake:
    def __init__(self, screen, x, y, width, max_x, max_y):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.speed = 10
        self.max_x = max_x
        self.max_y = max_y
        self.direction = ""
        self.length = 1
        self.body = []
        self.body.append((self.x, self.y))

    def draw(self):
        for i in self.body:
            pygame.draw.rect(self.screen, (0, 255, 0), (i[0], i[1], self.width, self.width))

    def set_direction(self, direction):
        if direction == "right" and self.direction != "left":
            self.direction = "right"
        if direction == "left" and self.direction != "right":
            self.direction = "left"
        if direction == "up" and self.direction != "down":
            self.direction = "up"
        if direction == "down" and self.direction != "up":
            self.direction = "down"

    def move(self):
        if self.direction == "right":
            self.x += self.speed
        if self.direction == "left":
            self.x -= self.speed
        if self.direction == "up":
            self.y -= self.speed
        if self.direction == "down":
            self.y += self.speed
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]

    def detect_collision(self):
        if self.x < 0:
            return True
        if self.x > self.max_x - self.width:
            return True
        if self.y < 0:
            return True
        if self.y > self.max_y - self.width:
            return True
        return False

    def detect_collision_self(self):
        # detect if the head of the snake is colliding with the body
        # we exclude the last element of the body because it is the head
        for i in self.body[:-1]:
            if self.x == i[0] and self.y == i[1]:
                return True
        return False

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.width)

    def add_body(self):
        self.body.append((self.x, self.y))

    def eat(self, food, wall):
        collide = self.get_rect().colliderect(food.get_rect())
        if collide:
            self.length += 1
            self.add_body()
            food.spawn_food(self, wall)
            return True

    def upgrade_speed(self):
        self.speed += 0.5

    def reset(self):
        self.x = 250
        self.y = 250
        self.length = 1
        self.body = []
        self.body.append((self.x, self.y))
        self.direction = "right"