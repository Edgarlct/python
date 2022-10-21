import pygame
import csv

class Score:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0

    def draw(self):
        font = pygame.font.SysFont("arial", 30)
        text = font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.screen.blit(text, (0, 0))

    def add_score(self):
        self.score += 1
        if self.score % 3 == 0 and self.score != 0:
            return True

    def reset_score(self):
        self.score = 0

    def save_name(self, event, textinput):
        textinput.update(event)
        textinput.font_color = (255, 255, 255)
        textinput.cursor_color = (255, 255, 255)
        self.screen.blit(textinput.surface, (0, 100))

    def save_score(self, name):
        # save the score in a csv file
        with open("scores.csv", "a") as file:
            writer = csv.writer(file)
            writer.writerow([name, self.score])

    def get_scores(self):
        # get the scores from the csv file
        with open("scores.csv", "r") as file:
            reader = csv.reader(file)
            scores = list(reader)
        return scores

    def draw_high_score(self, scores):
        # draw the high scores
        font = pygame.font.SysFont("arial", 12)
        text = font.render("High Scores", True, (255, 255, 255))
        self.screen.blit(text, (0, 150))
        for i in range(len(scores)):
            text = font.render(scores[i][0] + " - " + scores[i][1], True, (255, 255, 255))
            self.screen.blit(text, (0, 200 + 20 * i))
