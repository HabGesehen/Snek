import pygame
import sys
import random
from pygame.math import Vector2

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    def update(self):
        self.snake.moveSnake()
        self.collision()
        self.fail()
    def draw(self):
        self.fruit.drawFruit()
        self.snake.drawSnake()
        self.drawScore()
    def collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add()
    def fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def drawScore(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(99,98,97))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface,score_rect)

    def game_over(self):
        # Reset snake and fruit
        self.snake = SNAKE()
        self.fruit = FRUIT()
        # Restart game loop
        self.run()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    self.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0,-1)
                    if event.key == pygame.K_w:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0,-1)
                    if event.key == pygame.K_RIGHT:
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1,0)
                    if event.key == pygame.K_d:
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1,0)
                    if event.key == pygame.K_DOWN:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0,1)
                    if event.key == pygame.K_s:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0,1)
                    if event.key == pygame.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1,0)
                    if event.key == pygame.K_a:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1,0)
            screen.fill((70,207,107))
            self.draw()
            pygame.display.update()
            clock.tick(60)


pygame.init()
cell_size = 30
cell_number = 15
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font('font.ttf', 50)
pygame.display.set_caption('SNek')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    screen.fill((70,207,107))
    main_game.draw()
    pygame.display.update()
    clock.tick(60)