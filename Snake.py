import sys, random
from pygame.math import Vector2
import pygame as pg


class Main:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.food.draw_food()
        self.snake.draw_snake()

    def check_collision(self):
        if self.food.pos == self.snake.body[0]:
            self.food.randomize()
            self.snake.add_block()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    def game_over(self):
        pg.quit()
        sys.exit()
class Snake:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            block_rect = pg.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            pg.draw.rect(screen, (183, 111, 122), block_rect)

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True


class Food:
    def __init__(self):
        self.randomize()

    def draw_food(self):
        food_rect = pg.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, food_rect)
        # pg.draw.rect(screen, (126, 166, 114), food_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


pg.init()
cell_size = 40
cell_number = 20
screen = pg.display.set_mode((cell_size * cell_number, cell_size * cell_number))
clock = pg.time.Clock()
game = True
apple = pg.image.load('image/apple.png').convert_alpha()

main_game = Main()

SCREEN_UPDATE = pg.USEREVENT
pg.time.set_timer(SCREEN_UPDATE, 150)

while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pg.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, +1)
            if event.key == pg.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(+1, 0)
            if event.key == pg.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pg.display.update()
    clock.tick(60)