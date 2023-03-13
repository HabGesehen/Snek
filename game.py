import pygame
import sys
import random
from pygame.math import Vector2

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.newblock = False

    def drawSnake(self):
        for block in self.body:
            block_rect = pygame.Rect(int(block.x * cell_size),int(block.y * cell_size),cell_size,cell_size)
            pygame.draw.rect(screen,(54,98,194),block_rect)

    def moveSnake(self):
        if self.newblock == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.newblock = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
    def add(self):
        self.newblock = True
    

class FRUIT:
    def __init__(self):
        self.randomize()

    def drawFruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        pygame.draw.rect(screen,(207,70,77),fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0,cell_number - 1)
        self.y = random.randint(0,cell_number - 1)
        self.pos = pygame.math.Vector2(self.x,self.y)

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
        score_surface = game_font1.render(score_text,True,(99,98,97))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface,score_rect)

    def game_over(self):
        restart_surface = game_font2.render('Press SPACE to restart',True,(0,0,0))
        restart_rect = restart_surface.get_rect(center = (cell_number*cell_size/2,cell_number*cell_size/2+30))
        screen.blit(restart_surface,restart_rect)
        pygame.display.update()
        waiting = True
        while waiting:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        waiting = False
                        self.snake = SNAKE()


pygame.init()
cell_size = 30
cell_number = 15
screen = pygame.display.set_mode((cell_number * cell_size,cell_number * cell_size))
clock = pygame.time.Clock()
game_font1 = pygame.font.Font('font.ttf', 35)
game_font2 = pygame.font.Font('font.ttf', 16)
pygame.display.set_caption('Snek')
ico = pygame.image.load('ico.png')
pygame.display.set_icon(ico)

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