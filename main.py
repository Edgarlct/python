import pygame
import Snake
import Food
import Score
import Message
import Wall
import pygame_textinput

module_charge = pygame.init()
print(module_charge)


def play():
    screen = pygame.display.set_mode((500, 500))

    game_play = True
    game_stop = False

    snake = Snake.Snake(screen, 250, 250, 20, 500, 500)
    food = Food.Food(screen, 10, 500, 500)
    score = Score.Score(screen)
    message = Message.Message(screen)
    wall = Wall.Wall(screen, 20, 20)

    clock = pygame.time.Clock()
    textinput = pygame_textinput.TextInputVisualizer()
    high_score = score.get_scores()
    while game_play:
        # reset screen
        screen.fill((0, 0, 0))

        # draw score
        score.draw()

        # draw snake and food and wall
        snake.draw()
        food.draw()
        wall.draw()

        # snake movement
        snake.move()

        # detect collision
        if snake.detect_collision_self() or snake.detect_collision() or wall.detect_collision(snake):
            game_play = False
            game_stop = True

        # snake eat food
        eat = snake.eat(food, wall)
        if eat:
            need_wall = score.add_score()
            if need_wall:
                wall.add_wall(snake)


        if score.score >= 5:
            food.move_food(wall, snake)

        # define snake direction
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_play = False
                if event.key == pygame.K_RIGHT:
                    snake.set_direction("right")
                if event.key == pygame.K_LEFT:
                    snake.set_direction("left")
                if event.key == pygame.K_UP:
                    snake.set_direction("up")
                if event.key == pygame.K_DOWN:
                    snake.set_direction("down")

            if event.type == pygame.QUIT:
                game_play = False

        clock.tick(20)
        pygame.display.flip()

        # game stop
        while game_stop:
            screen.fill((0, 0, 0))
            event = pygame.event.get()

            message.set_text("Game Over, press ESC to exit, press SPACE to restart")
            message.draw()
            score.draw()
            score.save_name(event, textinput)
            score.draw_high_score(high_score)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if textinput.value != "":
                            score.save_score(textinput.value)
                            high_score = score.get_scores()
                            textinput.value = ""
                    if event.key == pygame.K_ESCAPE:
                        game_stop = False
                        game_play = False
                    if event.key == pygame.K_SPACE:
                        game_play = True
                        game_stop = False
                        snake.reset()
                        score.reset_score()
                        wall.reset()
                        food.reset()
                        print("Restarting game")
                if event.type == pygame.QUIT:
                    game_stop = False

            pygame.display.flip()


play()
pygame.quit()
